"""
Este script ilustra el concepto de **herencia selectiva** en Python mediante las clases `Parent` y `Child`.

- **Herencia selectiva**: La clase hija (`Child`) hereda selectivamente atributos y métodos de la clase padre (`Parent`). Aunque el constructor de la clase padre incluye un atributo opcional (`profession`), este atributo no se hereda ni se utiliza en la clase hija.
- **Extensión de funcionalidad**: La clase hija define nuevos atributos (`school` y `grade`) y un método específico (`student_intro`) que complementan la funcionalidad básica proporcionada por la clase padre.
- **Caso de uso**: La herencia selectiva es útil cuando solo una parte de los atributos o métodos de la clase base son relevantes para la clase derivada.
"""

class Parent():
    def __init__(self, name, age, profession=None):
        self.name = name
        self.age = age
        self.profession = profession
        
    def introduction(self):
        print(f"Mi nombre es {self.name}, tengo {self.age} años.")  # Traducción: My name is {self.name}, I am {self.age} years old.


class Child(Parent):
    # Agregar atributos específicos: school y grade
    def __init__(self, name, age, school, grade):
        self.school = school
        self.grade = grade
        
        # Invocar los atributos name y age de la clase Parent (sin incluir profession)
        Parent.__init__(self, name, age)
        
    # Crear función específica para la clase Child
    def student_intro(self):
        print(f"Voy a la escuela {self.school} y estoy en el grado {self.grade}.")  # Traducción: I go to {self.school} school and I am in grade {self.grade}.


if __name__ == "__main__":
    print("")
    # Crear objeto Parent:
    juanfer = Parent('Juan Fernando', 65, 'Manager')
    juanfer.introduction()  # Usar el método de la clase Parent
    print("")

    # Crear objeto Child:
    nico = Child('nico', 24, 'roosevelt', 10)
    nico.introduction()       # El objeto nico usa una función de la clase Parent
    nico.student_intro()      # El objeto nico llama a una función de su propia clase
    print("")