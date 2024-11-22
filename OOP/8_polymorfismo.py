"""
Este script ilustra el concepto de **polimorfismo** en programación orientada a objetos. 

- **Polimorfismo**: Es la capacidad de una función o método de tomar diferentes formas. En Python, esto significa que el mismo nombre de método puede tener comportamientos diferentes dependiendo del objeto que lo invoque. 
- En este ejemplo, dos clases diferentes (`India` y `USA`) tienen métodos con el mismo nombre (`capital`, `language`, `type`), pero implementados de manera diferente para cada clase. El mismo código puede usarse para invocar estos métodos en objetos de diferentes clases, demostrando cómo el polimorfismo permite tratar objetos de diferentes tipos de manera uniforme.

En este caso, ambos objetos de diferentes clases (India y USA) usan el mismo conjunto de métodos sin importar la clase específica a la que pertenecen.
"""

class India():
    def capital(self):
        print("New Delhi es la capital de la India.")  # Traducción: New Delhi is the capital of India.
 
    def language(self):
        print("Hindi es el idioma más hablado de la India.")  # Traducción: Hindi is the most widely spoken language of India.
 
    def type(self):
        print("La India es un país en desarrollo.")  # Traducción: India is a developing country.
 
class USA():
    def capital(self):
        print("Washington, D.C. es la capital de los EE.UU.")  # Traducción: Washington, D.C. is the capital of USA.
 
    def language(self):
        print("El inglés es el idioma principal de los EE.UU.")  # Traducción: English is the primary language of USA.
 
    def type(self):
        print("EE.UU. es un país desarrollado.")  # Traducción: USA is a developed country.
 
print("")

# Crear objetos de ambas clases
obj_ind = India()
obj_usa = USA()

# La función usa dos tipos de clases diferentes (India y USA) de la misma manera.
for country in (obj_ind, obj_usa):
    country.capital()     # Python llama al mismo método en ambas clases
    country.language()    # No importa en qué clase pertenece el método
    country.type()
print("")