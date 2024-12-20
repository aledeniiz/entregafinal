# Sistema de Gestión de Envíos de Paquetes

## Descripción del Proyecto
Este programa implementa un **sistema completo de gestión de envíos de paquetes** utilizando Python. El sistema permite registrar, rastrear, listar y eliminar paquetes, además de calcular rutas óptimas y tiempos de envío entre ciudades de la Península Ibérica. Se utiliza un grafo ponderado para modelar las conexiones entre las ciudades y el algoritmo de **Dijkstra** para encontrar rutas más eficientes.

Este software es ideal como solución de logística básica y demostración de conceptos avanzados de programación.

---

## Funcionalidades Principales

1. **Cálculo del tiempo de envío**:
   - Calcula el tiempo estimado entre dos ciudades basado en su distancia y una velocidad promedio.

2. **Cálculo de la ruta más corta**:
   - Implementa el **algoritmo de Dijkstra** usando `NetworkX` para encontrar la ruta óptima entre dos ciudades.

3. **Visualización del grafo**:
   - Muestra gráficamente las conexiones y distancias entre las ciudades utilizando `Matplotlib`.

4. **Gestión de paquetes**:
   - Permite **registrar**, **rastrear**, **listar** y **eliminar paquetes**.
   - La información de los paquetes se almacena en un archivo `JSON` para asegurar la **persistencia de datos**.

5. **Interfaz interactiva**:
   - Menú intuitivo para que el usuario seleccione opciones fácilmente.

---

## Bibliotecas Utilizadas

1. **NetworkX**:
   - Utilizada para modelar las ciudades y sus conexiones como un grafo ponderado.
   - Facilita la implementación eficiente del algoritmo de Dijkstra.

2. **Matplotlib**:
   - Proporciona la visualización gráfica del grafo, mostrando los nodos (ciudades) y las aristas (conexiones con sus distancias).

3. **JSON**:
   - Maneja la persistencia de datos almacenando el registro de paquetes en un archivo externo.

4. **Sys**:
   - Permite manejar entornos interactivos y no interactivos.

---

## Estructura del Código

### Funciones Principales:
- **`generar_grafo_ciudades`**:
   - Crea un grafo con ciudades y sus distancias.

- **`mostrar_grafo_visual`**:
   - Visualiza el grafo utilizando `Matplotlib`.

- **`calcular_tiempo_envio`**:
   - Calcula el tiempo estimado de envío entre dos ciudades.

- **`calcular_ruta_mas_corta`**:
   - Encuentra la ruta más corta entre dos ciudades utilizando el algoritmo de Dijkstra.

- **`registrar_paquete`**:
   - Registra un paquete en el sistema, calculando automáticamente la ruta más corta.

- **`rastrear_paquete`**:
   - Muestra el estado actual de un paquete según su código único.

- **`listar_paquetes`**:
   - Lista todos los paquetes registrados con sus detalles.

- **`eliminar_paquete`**:
   - Permite eliminar un paquete utilizando su código.

### Menú Interactivo:
El programa cuenta con un menú que permite al usuario seleccionar las siguientes opciones:

1. Calcular tiempo de envío entre dos ciudades.
2. Calcular la ruta más corta entre dos ciudades.
3. Mostrar grafo visual.
4. Registrar un paquete.
5. Rastrear un paquete.
6. Listar todos los paquetes.
7. Eliminar un paquete.
8. Salir.

---

## Algoritmo de Dijkstra
El **algoritmo de Dijkstra** es un método eficiente para encontrar la ruta más corta en un grafo ponderado con pesos positivos. En este programa:
- Las ciudades se modelan como nodos.
- Las conexiones entre ciudades (con distancias) son las aristas con pesos.
- Utilizamos las funciones `nx.shortest_path` y `nx.shortest_path_length` de **NetworkX**, que implementan Dijkstra internamente.

Ejemplo de salida:
```
La ruta más corta entre Madrid y Barcelona es: Madrid -> Zaragoza -> Barcelona
Distancia total: 621 km
```

---

## Persistencia de Datos
El sistema almacena y recupera la información de los paquetes en un archivo `registro_paquetes.json`. Cada paquete contiene:
- Código único (ej: PKG-00001).
- Ciudad de origen.
- Ciudad de destino.
- Ruta calculada entre las ciudades.
- Distancia total.
- Estado del paquete (ej: "En tránsito").

Ejemplo de entrada en `registro_paquetes.json`:
```json
[
  {
    "codigo": "PKG-00001",
    "origen": "Madrid",
    "destino": "Barcelona",
    "ruta": ["Madrid", "Zaragoza", "Barcelona"],
    "distancia_total": 621,
    "estado": "En tránsito"
  }
]
```

---

## Ejecución del Programa
1. Asegúrate de tener las bibliotecas instaladas:
   ```bash
   pip install networkx matplotlib
   ```

2. Ejecuta el programa:
   ```bash
   python nombre_del_archivo.py
   ```

3. Sigue las instrucciones en pantalla para interactuar con el menú.

---

## Conclusión
Este programa demuestra el uso de **algoritmos de grafos**, persistencia de datos y visualización gráfica en un sistema de logística. Al combinar la potencia de **NetworkX**, **Matplotlib** y el manejo eficiente de datos con **JSON**, se crea una herramienta funcional y escalable que puede ampliarse para resolver problemas más complejos en logística de envíos.


