"""
Este script demuestra el concepto de **miembros privados** en programación orientada a objetos. 

- En Python, los miembros privados son aquellos que no deben ser accesibles fuera de la clase, y se denotan mediante un doble guión bajo (`__`). 
- Sin embargo, Python realiza un *name mangling*, es decir, transforma internamente el nombre del miembro privado para hacerlo inaccesible desde fuera de la clase directamente. 
- Intentar acceder a un miembro privado de una clase desde una instancia o desde una clase derivada resultará en un error.

En este ejemplo, el atributo `__c` de la clase `Base` es privado y no puede ser accedido ni por objetos de la clase `Base` ni por objetos de la clase derivada `Derived`.
"""

class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"    # Atributo público
        self.__c = "GeeksforGeeks"  # Atributo privado
  
# Creando una clase derivada 
class Derived(Base): 
    def __init__(self): 
  
        # Llamando al constructor de la clase Base 
        Base.__init__(self) 
        print("Llamando al miembro privado de la clase base: ") 
        print(self.__c)  # Esto generará un error de atributo
  
  
# Código principal 
obj1 = Base() 
print(obj1.a)  # Esto es válido
print(obj1.__c)  # Esto generará un error de atribución: Base no tiene el atributo __c

obj2 = Derived()  # Esto generará un error de atribución ya que __c es un miembro privado de la clase base