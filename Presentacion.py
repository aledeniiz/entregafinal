import networkx as nx
import matplotlib.pyplot as plt
import sys
import json

# Registro global de paquetes
registro_paquetes = []

# Funciones auxiliares

def guardar_registro_paquetes():
    """Guarda el registro de paquetes en un archivo JSON."""
    with open("registro_paquetes.json", "w") as archivo:
        json.dump(registro_paquetes, archivo, indent=4)

def cargar_registro_paquetes():
    """Carga el registro de paquetes desde un archivo JSON."""
    global registro_paquetes
    try:
        with open("registro_paquetes.json", "r") as archivo:
            registro_paquetes = json.load(archivo)
    except FileNotFoundError:
        registro_paquetes = []

# Función para generar el grafo

def generar_grafo_ciudades():
    """
    Genera un grafo con las distancias reales aproximadas entre ciudades de la península ibérica.
    """
    grafo = {
        "Madrid": {"Barcelona": 621, "Valencia": 355, "Sevilla": 532, "Lisboa": 625, "Bilbao": 400},
        "Barcelona": {"Madrid": 621, "Valencia": 350, "Bilbao": 610, "Zaragoza": 313},
        "Valencia": {"Madrid": 355, "Barcelona": 350, "Sevilla": 650},
        "Sevilla": {"Madrid": 532, "Valencia": 650, "Lisboa": 460},
        "Lisboa": {"Madrid": 625, "Sevilla": 460, "Porto": 313},
        "Bilbao": {"Madrid": 400, "Barcelona": 610, "Zaragoza": 320},
        "Zaragoza": {"Barcelona": 313, "Bilbao": 320, "Madrid": 325},
        "Porto": {"Lisboa": 313}
    }
    return grafo

# Visualización del grafo

def mostrar_grafo_visual(grafo):
    """
    Visualiza el grafo de ciudades con distancias usando NetworkX y Matplotlib.
    """
    G = nx.Graph()
    for ciudad, conexiones in grafo.items():
        for otra_ciudad, distancia in conexiones.items():
            G.add_edge(ciudad, otra_ciudad, weight=distancia)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    plt.title("Distancias entre Ciudades de la Península Ibérica")
    plt.show()

# Cálculo de tiempo de envío

def calcular_tiempo_envio(grafo, origen, destino, velocidad=80):
    """
    Calcula el tiempo estimado de envío entre dos ciudades.
    """
    if origen in grafo and destino in grafo[origen]:
        distancia = grafo[origen][destino]
        tiempo = distancia / velocidad
        print(f"\nLa distancia entre {origen} y {destino} es de {distancia} km.")
        print(f"El tiempo estimado de entrega es de {tiempo:.2f} horas (a {velocidad} km/h).\n")
        return distancia, tiempo
    else:
        print(f"No hay datos disponibles entre {origen} y {destino}.")
        return None, None

# Cálculo de la ruta más corta

def calcular_ruta_mas_corta(grafo, origen, destino):
    """
    Calcula la ruta más corta entre dos ciudades usando el algoritmo de Dijkstra.
    """
    G = nx.Graph()
    for ciudad, conexiones in grafo.items():
        for otra_ciudad, distancia in conexiones.items():
            G.add_edge(ciudad, otra_ciudad, weight=distancia)

    try:
        ruta = nx.shortest_path(G, source=origen, target=destino, weight='weight')
        distancia_total = nx.shortest_path_length(G, source=origen, target=destino, weight='weight')
        print(f"La ruta más corta entre {origen} y {destino} es: {' -> '.join(ruta)}")
        print(f"Distancia total: {distancia_total} km\n")
        return ruta, distancia_total
    except nx.NetworkXNoPath:
        print(f"No existe una ruta entre {origen} y {destino}.")
        return None, None

# Rastrear paquetes

def rastrear_paquete(codigo):
    """
    Muestra el estado actual de un paquete dado su código.
    """
    paquete = next((p for p in registro_paquetes if p['codigo'] == codigo), None)
    if paquete:
        print(f"\nEstado del paquete {codigo}:")
        print(f"Origen: {paquete['origen']}")
        print(f"Destino: {paquete['destino']}")
        print(f"Ruta: {' -> '.join(paquete['ruta'])}")
        print(f"Estado: {paquete['estado']}\n")
    else:
        print(f"No se encontró el paquete con código {codigo}.\n")

# Crear un nuevo paquete

def registrar_paquete(origen, destino, grafo):
    """
    Registra un nuevo paquete en el sistema.
    """
    ruta, distancia_total = calcular_ruta_mas_corta(grafo, origen, destino)
    if ruta:
        codigo = f"PKG-{len(registro_paquetes) + 1:05d}"
        paquete = {
            "codigo": codigo,
            "origen": origen,
            "destino": destino,
            "ruta": ruta,
            "distancia_total": distancia_total,
            "estado": "En tránsito"
        }
        registro_paquetes.append(paquete)
        guardar_registro_paquetes()
        print(f"\nPaquete registrado exitosamente con código: {codigo}\n")
    else:
        print("No se pudo registrar el paquete debido a una ruta inexistente.\n")

# Mostrar lista de paquetes

def listar_paquetes():
    """
    Lista todos los paquetes registrados.
    """
    if registro_paquetes:
        print("\n--- Lista de Paquetes ---")
        for paquete in registro_paquetes:
            print(f"Código: {paquete['codigo']}")
            print(f"  Origen: {paquete['origen']}")
            print(f"  Destino: {paquete['destino']}")
            print(f"  Ruta: {' -> '.join(paquete['ruta'])}")
            print(f"  Estado: {paquete['estado']}\n")
    else:
        print("\nNo hay paquetes registrados.\n")

# Eliminar un paquete

def eliminar_paquete(codigo):
    """
    Elimina un paquete del registro dado su código.
    """
    global registro_paquetes
    paquete = next((p for p in registro_paquetes if p['codigo'] == codigo), None)
    if paquete:
        registro_paquetes.remove(paquete)
        guardar_registro_paquetes()
        print(f"\nPaquete con código {codigo} eliminado exitosamente.\n")
    else:
        print(f"\nNo se encontró el paquete con código {codigo}.\n")

# Menú principal

def mostrar_menu():
    """
    Muestra un menú de opciones para el usuario.
    """
    print("\n--- Menú de Opciones ---")
    print("1. Calcular tiempo de envío entre dos ciudades")
    print("2. Calcular la ruta más corta entre dos ciudades")
    print("3. Mostrar grafo visual")
    print("4. Registrar un paquete")
    print("5. Rastrear un paquete")
    print("6. Listar todos los paquetes")
    print("7. Eliminar un paquete")
    print("8. Salir")

def obtener_input_ciudades(predefinido=False):
    """
    Permite al usuario ingresar ciudades en un entorno seguro.
    Si predefinido=True, utiliza valores predeterminados.
    """
    if predefinido:
        return "Madrid", "Barcelona"
    try:
        origen = input("Ingrese la ciudad de origen: ").title()
        destino = input("Ingrese la ciudad de destino: ").title()
    except (EOFError, OSError):
        print("\nEl entorno no permite entradas, utilizando valores predeterminados.\n")
        return "Madrid", "Barcelona"
    return origen, destino

# ----------- MAIN -----------
if __name__ == "__main__":
    grafo_ciudades = generar_grafo_ciudades()
    cargar_registro_paquetes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            origen, destino = obtener_input_ciudades()
            calcular_tiempo_envio(grafo_ciudades, origen, destino)
        elif opcion == "2":
            origen, destino = obtener_input_ciudades()
            calcular_ruta_mas_corta(grafo_ciudades, origen, destino)
        elif opcion == "3":
            mostrar_grafo_visual(grafo_ciudades)
        elif opcion == "4":
            origen, destino = obtener_input_ciudades()
            registrar_paquete(origen, destino, grafo_ciudades)
        elif opcion == "5":
            codigo = input("Ingrese el código del paquete: ")
            rastrear_paquete(codigo)
        elif opcion == "6":
            listar_paquetes()
        elif opcion == "7":
            codigo = input("Ingrese el código del paquete a eliminar: ")
            eliminar_paquete(codigo)
        elif opcion == "8":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
