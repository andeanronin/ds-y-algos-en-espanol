# Encontrar todos los números que faltan en un arreglo

"""
Dado un arreglo nums de n enteros, donde nums[i] está en el rango [1, n],  
devuelve un arreglo con todos los enteros en el rango [1, n] que no aparecen en nums. 

Ejemplo:
    - entrada: nums = [4, 3, 2, 7, 8, 2, 3, 1]
    - salida: 5, 6
    - rango: [1, 8]

Crear una lista ordenada con los números en el rango dado, all_nums = [1, 2, 3, 4, 5, 6, 7, 8]
- Convertir nums a un conjunto: nums = set(nums)
- Ordenar el conjunto: sort(set) 
Iterar sobre nums, obtener el valor i, iterar sobre la lista del rango, eliminar el valor de la lista del rango.
Cualquier número que quede en all_nums es un número que falta.  
"""

nums = [4, 3, 2, 7, 8, 2, 3, 1] # tamaño = 8

def solution(inputnums):
    # Crear una lista de comparación con el rango de números
    comparison_list = list(range(1, len(inputnums) + 1))
    print('lista de comparación: ', comparison_list)

    # Convertir nums a un conjunto para eliminar duplicados
    set_nums = set(inputnums)
    print('conjunto de nums: ', set_nums)
    
    # Remover los números que están en el conjunto de la lista de comparación
    for i in set_nums:
        comparison_list.remove(i)
    
    # Imprimir los valores que faltan
    print('valores faltantes: ', comparison_list)

solution(nums)

def solution_two(nums):
    # Crear un conjunto con el rango completo de números
    full_set = set(range(1, len(nums) + 1))

    # Convertir nums a un conjunto para eliminar duplicados
    set_nums = set(nums)

    # Calcular la diferencia para encontrar los valores que faltan
    missing_values = full_set - set_nums

    return missing_values

print(solution_two(nums))