"""
Algoritmo de Búsqueda Lineal:
LinearSearch(arreglo, clave)
   Para cada elemento en el arreglo
        Si el elemento == valor
            retorna su índice

Programa de Búsqueda Lineal
"""

def LinearSearch(array, k):
    for j in range(len(array)):  # Itera sobre cada elemento en el arreglo
        if (array[j] == k):  # Si el elemento actual es igual a la clave buscada
            return j  # Retorna el índice del elemento
    return -1  # Si no se encuentra el elemento, retorna -1

if __name__ == "__main__":
    # Buscando el valor k en el arreglo:
    array = [1, 3, 5, 7, 9]  # Arreglo de ejemplo
    k = 8  # Valor a buscar
    result = LinearSearch(array, k)  # Llama a la función LinearSearch
    if(result == -1):
        print("Elemento no encontrado")  # Si el resultado es -1, el elemento no se encuentra
    else:
        print("Elemento encontrado en el índice: ", result)  # Si se encuentra, muestra el índice