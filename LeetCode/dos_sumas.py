# Suma de Dos Números

"""
Dado un array de números enteros nums y un número entero objetivo, devuelve los índices de los dos números que suman el objetivo.

Puedes asumir que cada entrada tendrá exactamente una solución, y no puedes usar el mismo elemento dos veces.

Puedes devolver la respuesta en cualquier orden.

Ejemplos:

Entrada: nums = [2,7,11,15], objetivo = 9
Salida: [0,1]
"""
nums = [2,7,11,15]

target = 13

def solution(nums):
    # Solución de fuerza bruta
    for i in range(0, len(nums)):
        diff = target - nums[i] 
        if diff in nums:
            # Imprime los índices que suman el objetivo
            print(nums.index(diff), i)
            return

solution(nums)
            

def solution_two(nums, target):
    # Solución utilizando un diccionario hash (mapa hash)
    hashMap = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in hashMap:
            # Si se encuentra la diferencia en el mapa hash, devuelve los índices
            return (index, hashMap[diff])
        
        # Agrega el valor al mapa hash si la diferencia no está en el mapa
        hashMap[value] = index 

nums_2 = [2,7,11,15]
solv = solution_two(nums_2, 9)