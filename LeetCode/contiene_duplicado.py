# Dado un arreglo de enteros nums, retorna verdadero si algún valor aparece al menos dos veces en el arreglo.
# Retorna falso si cada valor es distinto.

# Ejemplo:
# - nums = [1, 2, 1, 4]  (retorna true)
# - nums = [2, 5, 8, 9] (retorna false)

miArreglo = [1, 1, 5, 9] 


def containsDuplicate(nums):
    # Compara la longitud del arreglo original con la longitud del conjunto (valores únicos)
    if len(nums) == len(set(nums)):
        return False
    else:
        return True 

print(containsDuplicate(miArreglo))