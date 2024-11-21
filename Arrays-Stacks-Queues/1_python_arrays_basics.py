from array import *

# 1. Creando un array de tipo 'i', es decir numeros de dos bytes
array_enteros = array('i', [10, 20, 30, 40, 50])

# 2. Recorrer el array:
for x in array_enteros:
    print(x)

# 3. Acceder a un elemento en el array
print("")
print("Elemento en el índice 2:")
print(array_enteros[2])
print("")

# 4. Insertar un elemento en el array
array_enteros.insert(1, 140)  # inserta 140 en el índice 1
for x in array_enteros:
    print(x)

# 5. Eliminar un elemento en el array
array_enteros.remove(140)
print("")
for x in array_enteros:
    print(x)
print("")
# 6. Buscar en un array
print("El índice de 50 es: ")
print(array_enteros.index(50))  # obtener el índice del elemento 50

# 7. Actualizar un array
array_integers[2] = 300 # changes the value at index 2 from 30 to 300