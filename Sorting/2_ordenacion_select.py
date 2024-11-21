"""
Resumen del Algoritmo Selection Sort:

¿Qué es Selection Sort?
Selection Sort es un algoritmo de ordenación simple que funciona encontrando el valor más pequeño en el arreglo y colocándolo al inicio. Luego, se repite el proceso para el resto del arreglo, moviendo el siguiente valor más pequeño en la siguiente posición, hasta que todo el arreglo esté ordenado. A pesar de ser intuitivo, tiene una eficiencia inferior a otros algoritmos más avanzados como Quicksort o Merge Sort, especialmente cuando se trabaja con grandes volúmenes de datos.

¿Cuándo se usa?
Selection Sort se utiliza en situaciones donde la simplicidad del algoritmo es más importante que la eficiencia, o cuando los arreglos son pequeños y no se requiere un rendimiento extremo. También es útil para aplicaciones educativas debido a su simplicidad.

Pros y Contras de Selection Sort:

Pros:
- Simplicidad: El algoritmo es fácil de entender e implementar.
- Espacio: No requiere espacio adicional, ya que ordena el arreglo in situ (en el lugar).

Contras:
- Eficiencia: Tiene un tiempo de ejecución de O(n²) en el peor de los casos, lo que lo hace lento para arreglos grandes.
- No estable: Selection Sort no es un algoritmo estable, lo que significa que puede cambiar el orden de los elementos con valores iguales.

Este algoritmo es útil para ordenar arreglos pequeños o cuando se necesita una implementación sencilla sin preocuparse por la eficiencia en tiempo.
"""

# Algoritmo de Selection Sort

def findSmallest(arr): 
    """
    Función que encuentra el valor más pequeño en un arreglo. 
    Entrada: arreglo
    Salida: valor más pequeño
    Método: comienza en el índice 0 y compara cada siguiente ítem
            Almacena el ítem más pequeño en la variable "smallest"
    """
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: 
            smallest = arr[i] 
            smallest_index = i
    return smallest_index


def selectionSort(arr): 
    """
    Función que ordena un arreglo de menor a mayor
    Entrada: arreglo
    Salida: arreglo ordenado de menor a mayor
    Método: itera a través del arreglo, obtiene el ítem más pequeño y lo almacena en un "Arreglo Ordenado"
            itera nuevamente a través del arreglo, obtiene el siguiente ítem más pequeño y lo almacena en el "Arreglo Ordenado"
            Repite hasta que no queden valores en el arreglo original y todos estén en el Arreglo Ordenado
    """
    sortedArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) 
        sortedArr.append(arr.pop(smallest)) 
    return sortedArr