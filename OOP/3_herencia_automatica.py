"""
Este script crea dos clases: una clase padre (`Father`) y una clase hija (`Child`). 

- **Herencia**: La clase hija hereda los atributos de instancia (`name`, `age`) y los métodos de la clase padre. Esto significa que la clase `Child` puede usar los métodos y atributos definidos en la clase `Father` sin necesidad de redefinirlos.
- **Método propio**: Aunque la clase `Child` no redefine el método `__init__`, hereda automáticamente los atributos de la clase padre. Además, `Child` define su propio método, `child_introduction`, para mostrar un mensaje único.
- **Uso común**: La herencia se usa para modelar relaciones jerárquicas y permite reutilizar el código de clases existentes.
"""

# Este archivo crea dos clases: una clase padre y una clase hija
# La clase hija hereda los atributos de instancia (name, age) y métodos de la clase padre

# Crear la clase padre
class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_attributes(self):
        print('Nombre: ', self.name)  # Traducción: Name
        print('Edad: ', self.age)    # Traducción: Age


# Crear la clase hija       
class Child(Father):
    # La clase hija no tiene un método __init__ propio, por lo que hereda automáticamente los atributos de instancia de la clase padre.

    def child_introduction(self):
        print(f"Soy un niño, me llamo {self.name} y tengo {self.age} años.")  # Traducción: I am a child my name is...


if __name__ == "__main__":
    print("")
    nicofather = Father('Miguel', 65)     # Crear objeto Father llamado nicofather
    nicofather.display_attributes()     # Ejecutar el método display_attributes() de la clase Father
    print("")

    # Crear objeto Child llamado nico    
    nico = Child('Angel', 24)   # Hereda las variables de instancia: name, age
    nico.display_attributes()  # Usar el método de la clase padre display_attributes()
    nico.child_introduction()  # Usar el método propio de la clase Child
    print("")