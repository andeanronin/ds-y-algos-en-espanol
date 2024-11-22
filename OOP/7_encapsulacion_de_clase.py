"""
Este script ilustra el concepto de **encapsulación en clases** en Python, específicamente mediante el uso de miembros protegidos.

- **Encapsulación**: En programación orientada a objetos, la encapsulación se refiere a restringir el acceso directo a los atributos de un objeto, manteniendo la integridad de los datos. Python lo implementa mediante convenciones de nombres.
- **Miembros protegidos**: En Python, un atributo protegido se define con un guion bajo inicial (`_`). Esto indica que no debe ser accedido directamente fuera de la clase o de sus subclases, aunque técnicamente no está restringido.
- **Caso de uso**: Los miembros protegidos son útiles para advertir a los desarrolladores de no modificar o acceder a ciertos atributos fuera de un contexto seguro.

En este ejemplo, se muestra cómo:
1. Un miembro protegido (`_protected_variable`) es definido en una clase base (`Base`) y accedido/modificado por una clase derivada (`Derived`).
2. Aunque se puede acceder a los miembros protegidos fuera de las clases, esto no es recomendable según la convención.
"""

# Programa en Python para demostrar miembros protegidos
  
# Crear una clase base 
class Base: 
    def __init__(self): 
        # Variable protegida 
        self._protected_variable = 2
  
# Crear una clase derivada 
class Derived(Base): 
    def __init__(self): 
        # Llamar al constructor de la clase Base
        Base.__init__(self) 
        print("Llamando al miembro protegido de la clase base: ",  self._protected_variable)  # Traducción: Calling protected member of base class
        
        # Modificar la variable protegida
        self._protected_variable = 3
        print("Llamando al miembro protegido modificado fuera de la clase: ", self._protected_variable)  # Traducción: Calling modified protected member outside class
  
print("")
derived_object = Derived()  # Imprime y modifica la variable protegida de la clase base
base_object = Base()  # No imprime nada

# Accediendo a la variable protegida de la clase base, lo cual en teoría no debería hacerse debido a la convención
print("")
print("Accediendo a la variable protegida del objeto base desde el objeto derivado: ", derived_object._protected_variable)  

# Accediendo al miembro protegido fuera de la clase directamente
print("Accediendo al miembro protegido del objeto base directamente: ", base_object._protected_variable) 