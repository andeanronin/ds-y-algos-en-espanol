"""
Este script demuestra un ejemplo de herencia funcional en Python. La herencia es un concepto fundamental en la programación orientada a objetos que permite a una clase (la clase hija) heredar métodos y propiedades de otra clase (la clase padre). Esto fomenta la reutilización de código y la estructura jerárquica. En este ejemplo, la clase `Parent` define un método que la clase `Child` hereda. Además, la clase `Child` puede tener métodos adicionales propios. Se utiliza la herencia para modelar relaciones "es-un" entre objetos y organizar el código de manera modular.
"""

class Parent(object):
    def function1(self):
        print("Esta función pertenece a la clase padre")  # Traducción: This function belongs to parent class
        
class Child(Parent):
    def function2(self):
        print("Esta función pertenece a la clase hija")  # Traducción: This function belongs to child class
     
# Crear una instancia de la clase hija  
nico = Child()
nico.function1()  # Llamando a la función 1 desde la clase hija
nico.function2()  # Llamando a la función 2 desde la clase hija