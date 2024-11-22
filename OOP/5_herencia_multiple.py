"""
Este script demuestra el concepto de **herencia múltiple** en Python, donde una clase derivada puede heredar atributos y métodos de múltiples clases base.

- **Herencia múltiple**: En este caso, la clase `Son` hereda de las clases `Mother` y `Father`. Esto permite a la clase derivada (`Son`) acceder y combinar atributos y métodos de ambas clases base.
- **Caso de uso**: La herencia múltiple es útil cuando un objeto necesita compartir o combinar características de varias fuentes (por ejemplo, atributos de ambos padres en un modelo familiar).
- **Ejemplo práctico**: En este ejemplo, la clase `Son` accede a los atributos y métodos de las clases `Mother` y `Father` para representar una relación de padres e hijos.
"""

# Clase base1
class Mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)  # Traducción: Imprime el nombre de la madre
 
# Clase base2
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)  # Traducción: Imprime el nombre del padre
 
# Clase derivada
class Son(Mother, Father):  # Hereda de 2 clases
    def parents(self):
        print("Padre:", self.fathername)  # Traducción: Father
        print("Madre:", self.mothername)  # Traducción: Mother
 
if __name__ == "__main__":
    print("")
    s1 = Son()
    s1.fathername = "RAM"    # Llama al atributo fathername y lo establece en "RAM"
    s1.mothername = "SITA"   # Llama al atributo mothername y lo establece en "SITA"
    s1.parents()             # Llama al método parents() de la clase derivada