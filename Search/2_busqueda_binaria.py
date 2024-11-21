"""
Búsqueda Binaria:
- La búsqueda binaria es un algoritmo eficiente para encontrar un valor en un arreglo ordenado.
- Funciona dividiendo repetidamente el rango de búsqueda por la mitad, reduciendo así el número de elementos que se deben verificar.
- Se usa cuando el arreglo está ordenado, y su eficiencia es O(log n), lo que la hace más rápida que la búsqueda lineal.
- El algoritmo puede implementarse de forma iterativa o recursiva.

Método Iterativo de Búsqueda Binaria:
"""

# Método de Búsqueda Binaria Iterativa:
def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

"""
Algoritmo de Búsqueda Binaria de Grokking:
- Esta es otra implementación del algoritmo de búsqueda binaria, diseñada como se describe en el libro 'Grokking Algorithms'.
- También utiliza un enfoque iterativo, ajustando los punteros low y high según la comparación entre el valor medio y el ítem objetivo.
"""

# Algoritmo de Búsqueda Binaria de Grokking
def grokkings_binary_search(list, item): 
    low = 0
    high = len(list) - 1
    while low <= high: 
        mid = (low + high) 
        guess = list[mid] 
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else:
            low = mid + 1
    return None

""""
Búsqueda Binaria Usando Recursión:
- Esta es una versión recursiva del algoritmo de búsqueda binaria.
- El caso base verifica si el puntero high es mayor o igual que el puntero low.
- La recursión sigue reduciendo el rango de búsqueda hasta que se encuentra el objetivo o se agota el rango de búsqueda.
"""

# Búsqueda binaria usando recursión:
def RbinarySearch(arr, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return RbinarySearch(arr, k, low, mid-1)
        else:
            return RbinarySearch(arr, k, mid + 1, high)
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    k = 7  # Valor a buscar

    # Aplicando la Búsqueda Binaria Iterativa  
    result = binarySearch(arr, k, 0, len(arr)-1)
    if result != -1:
        print("El elemento está presente en el índice " + str(result))
    else:
        print("No encontrado")

    #  Aplicando la Búsqueda Binaria Recursiva
    result = RbinarySearch(arr, k, 0, len(arr)-1)
    if result != -1:
        print("El elemento está presente en el índice " + str(result))
    else:
        print("No encontrado")