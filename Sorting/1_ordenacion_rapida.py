"""
Resumen del Algoritmo Quicksort:

¿Qué es Quicksort?
Quicksort es un algoritmo de ordenación eficiente y rápido basado en el paradigma de "divide y vencerás". El principio básico es elegir un elemento como *pivote*, luego dividir el arreglo en dos sub-arreglos: uno con los elementos menores que el pivote y otro con los elementos mayores. Este proceso se repite recursivamente en los sub-arreglos hasta que todos los sub-arreglos contienen menos de dos elementos, lo que significa que están ordenados.

¿Cuándo se usa?
Quicksort es ampliamente utilizado debido a su eficiencia y su capacidad para manejar grandes volúmenes de datos. Es comúnmente usado en situaciones donde el rendimiento es crítico, como en bases de datos y sistemas de búsqueda.

Pros y Contras de Quicksort:

Pros:
- Eficiencia: Quicksort tiene un tiempo de ejecución promedio de O(n log n), lo que lo convierte en uno de los algoritmos de ordenación más rápidos.
- Espacio: A diferencia de otros algoritmos de ordenación como *Merge Sort*, Quicksort utiliza espacio adicional mínimo, lo que lo hace adecuado para arreglos grandes.
- Recursividad: Aprovecha la recursividad para dividir y conquistar, lo que lo hace fácil de implementar.

Contras:
- Peor caso: En el peor de los casos, Quicksort puede tener un rendimiento de O(n²), especialmente cuando se selecciona un pivote mal (como el primero o el último elemento en un arreglo ya ordenado).
- Estabilidad: Quicksort no es un algoritmo estable, lo que significa que puede cambiar el orden de los elementos con valores iguales.

Este algoritmo es generalmente preferido cuando se tiene un arreglo grande y no se conoce el orden previo de los datos, pero es importante tener en cuenta la selección adecuada del pivote para evitar el peor caso.
"""

# Algoritmo de Quicksort para ordenar un arreglo

def quicksort(array): 
    """
    Algoritmo para ordenar un arreglo
    Entrada: Arreglo desordenado
    Salida: Arreglo ordenado
    Algoritmo: elegir un pivote (típicamente un elemento aleatorio en el arreglo)
               crear un arreglo con los elementos menores que el pivote
               crear un arreglo con los elementos mayores que el pivote
               repetir estos 3 pasos hasta que los sub-arreglos tengan menos de 2 elementos
               agregar todos los arreglos juntos
    """
    if len(array) < 2:
        return array      # Caso base: los arreglos con 0 o 1 elemento ya están "ordenados."
    else:  
        pivot = array[0]  # Caso recursivo
        less = [i for i in array[1:] if i <= pivot]     # Sub-arreglo de todos los elementos menores que el pivote
        greater = [i for i in array[1:] if i > pivot]   # Sub-arreglo de todos los elementos mayores que el pivote
    
        return quicksort(less) + [pivot] + quicksort(greater) 

print(quicksort([10, 5, 2, 3]))  