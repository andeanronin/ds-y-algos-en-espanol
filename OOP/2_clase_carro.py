"""
Este script ilustra cómo crear y utilizar clases en Python para representar objetos del mundo real. En este caso, se modela un coche con propiedades como su color y kilometraje. La clase `Car` utiliza un método especial llamado `__init__` para inicializar sus atributos, y otro método especial `__str__` para definir cómo se representará el objeto como una cadena de texto. Este enfoque se utiliza para encapsular datos y comportamientos relacionados en una sola entidad (objeto), facilitando la organización y reutilización del código.
"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage 
    
    def __str__(self):
        return f"El coche {self.color} tiene {self.mileage} millas"  # Traducción: The {self.color} car has {self.mileage} miles
    

bluetoyota = Car("blue", 20000)

print(bluetoyota)

redtoyota = Car("red", 1000)

print(redtoyota)