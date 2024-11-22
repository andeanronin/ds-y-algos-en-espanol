"""
Este script demuestra cómo realizar la herencia manual en Python mediante el uso de la clase `Parent` y la clase `Child`. 

- **Herencia manual**: En lugar de depender de la inicialización automática de la clase base, el constructor de la clase hija (`__init__`) invoca explícitamente el constructor de la clase padre usando `Parent.__init__`. Esto permite extender las funcionalidades de la clase base mientras se añaden atributos o métodos específicos a la clase hija.
- **Caso de uso**: La herencia manual es útil cuando se necesita personalizar la inicialización de la clase hija manteniendo la funcionalidad de la clase base.
- **Ejemplo práctico**: La clase `Child` hereda los atributos `name` y `age` de la clase `Parent`, y agrega sus propios atributos `school` y `grade`. Además, puede usar los métodos de la clase padre y definir los suyos propios.
"""

class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduction(self):
        print(f"Mi nombre es {self.name}, tengo {self.age} años.")  # Traducción: My name is {self.name}, I am {self.age} years old.


class Child(Parent):
    def __init__(self, name, age, school, grade):
        self.school = school
        self.grade = grade
        
        # Invocar explícitamente las variables de instancia name y age de la clase Parent
        Parent.__init__(self, name, age) 
        
    def student_intro(self):
        print(f"Voy a la escuela {self.school} y estoy en el grado {self.grade}.")  # Traducción: I go to {self.school} school and I am in grade {self.grade}.



# Crear una instancia de la clase Child   
nico = Child('nico', 24, 'roosevelt', 10)
nico.introduction()  # El objeto nico usa una función de la clase Parent
nico.student_intro()  # El objeto nico llama a una función de su propia clase