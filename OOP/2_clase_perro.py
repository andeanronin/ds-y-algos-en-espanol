"""
Este script demuestra el uso de variables de clase y variables de instancia en Python a través de la clase `Dog`. 

- **Variable de clase**: Una variable de clase, como `bark`, es compartida por todas las instancias de la clase `Dog`. Representa un comportamiento o atributo común a todos los perros.
- **Variables de instancia**: Son únicas para cada instancia de la clase y se definen en el método `__init__`. En este caso, las variables `name`, `race` y `color` son atributos específicos de cada perro.
- **Método de instancia**: El método `add_trick` permite añadir trucos específicos a cada perro almacenándolos en la lista `tricks`, que es una variable de instancia. Cada perro puede tener su propia lista de trucos.
"""

class Dog:
    bark = print('¡GUAU GUAU GUAU!')  # Traducción: BARK BARK BARK
    # Esta es una variable de clase, compartida por todas las instancias de la clase Dog

    def __init__(self, name, race, color): 
        # Las variables de instancia son únicas para cada perro (instancia)
        self.name = name
        self.race = race
        self.color = color
        self.tricks = []   # Crea una lista vacía específica para cada perro

    def add_trick(self, trick):
        self.tricks.append(trick)  # Añade trucos a la lista de la instancia
    
myPuppy = Dog("terminator", "labrador", "black")

myPuppy.bark  # Accede a la variable de clase

print(myPuppy.name)  # Muestra el nombre del perro
print(myPuppy.race)  # Muestra la raza del perro

# Añade trucos específicos al perro
myPuppy.tricks.append('saltar')  # Traducción: jump
myPuppy.tricks.append('buscar')  # Traducción: fetch

print(myPuppy.tricks)  # Muestra los trucos del perro