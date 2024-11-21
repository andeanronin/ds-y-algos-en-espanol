# Este script crea una torre (stack) de círculos. 

# Importar la clase Torre 
from stack_datastructure import Stack

# Crear la clase Círculo:
class Circulo(object):
    def __init__(self):
        self.radio = 0
    
    def __str__(self):  # cuando el usuario imprime un objeto Círculo, muestra:
        return f"Círculo con un radio de {self.radio}"
    
    def actualizar_radio(self, radio):
        self.radio = radio
    
    def obtener_radio(self):
        return self.radio
    

# Crear un objeto torre de círculos:
torre_de_circulos = Stack()

# Crear círculos
circulo_uno = Circulo()
circulo_dos = Circulo()
circulo_tres = Circulo()

# Asignar radios a los círculos
circulo_uno.actualizar_radio(4)
print("Primer círculo creado:", circulo_uno)
print("")
circulo_dos.actualizar_radio(2)
circulo_tres.actualizar_radio(8)

# Agregar los círculos a la torre de círculos:
torre_de_circulos.agregar_elemento(circulo_uno)
torre_de_circulos.agregar_elemento(circulo_dos)
torre_de_circulos.agregar_varios(circulo_tres, 4)  # agrega el objeto círculo tres 4 veces (mismo objeto)

# Imprimir la torre de círculos
print("Torre de círculos:")
torre_de_circulos.imprimir_bonito()
