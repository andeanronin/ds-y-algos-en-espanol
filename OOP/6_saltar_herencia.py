"""
Este script muestra el concepto de **sobrescritura de herencia** en Python, donde una clase derivada redefine un método de la clase base para adaptarlo a sus necesidades específicas.

- **Sobrescritura de métodos**: La clase hija (`Child`) redefine el método `introduction()` de la clase padre (`Parent`) para omitir ciertas funcionalidades (como las condiciones relacionadas con el atributo `profession`) que no son relevantes para la clase hija.
- **Caso de uso**: La sobrescritura de métodos permite a las clases hijas personalizar o limitar la funcionalidad heredada de la clase base.
- **Extensión de funcionalidad**: Además de sobrescribir métodos, la clase hija puede agregar nuevos métodos y atributos únicos a sus necesidades, como `student_intro`, que es específico de `Child`.
"""

class Parent():
    def __init__(self, name, age, profession=None):
        self.name = name
        self.age = age
        self.profession = profession
        
    def introduction(self):
        print(f"Mi nombre es {self.name}, tengo {self.age} años.")  # Traducción: My name is {self.name}, I am {self.age} years old.
        if self.profession is None:
            print("Estoy jubilado.")  # Traducción: I am retired.
        else:
            print(f"Soy un {self.profession}.")  # Traducción: I am a {self.profession}.


class Child(Parent):
    def __init__(self, name, age, school, grade):
        self.school = school
        self.grade = grade
        
        # Invocar los atributos name y age de la clase Parent (sin incluir profession)
        Parent.__init__(self, name, age)
        
    def introduction(self):
        # Sobrescribe el método introduction() para excluir las declaraciones condicionales no necesarias en la clase Child
        print(f"Mi nombre es {self.name}, tengo {self.age} años.")  # Traducción: My name is {self.name}, I am {self.age} years old.
    
    def student_intro(self):
        print(f"Voy a la escuela {self.school} y estoy en el grado {self.grade}.")  # Traducción: I go to {self.school} school and I am in grade {self.grade}.


if __name__ == "__main__":
    print("")
    # Crear objeto Parent:
    juanfer = Parent('Juan Fernando', 65, 'Manager')
    juanfer.introduction()  # Llama al método de la clase Parent
    print("")

    # Crear instancia de la clase Child:
    nico = Child('nico', 24, 'roosevelt', 10)
    nico.introduction()       # El objeto nico usa el método sobrescrito de la clase Child
    nico.student_intro()      # El objeto nico llama a un método específico de su clase
    print("")