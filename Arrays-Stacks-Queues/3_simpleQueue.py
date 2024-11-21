"""
Clase Simple de Cola (Queue)
    - Una cola (Queue) es una estructura de datos lineal que sigue el principio FIFO (First In, First Out), 
    - es decir, el primer elemento en entrar es el primero en salir. 
    - Se utiliza para gestionar tareas o procesos en orden, como una fila en un supermercado o una lista de reproducción de música.
"""


class Cola:
    def __init__(self): 
        self.cola = list()  # cada objeto de Cola se inicializa con una lista / array vacío

    # Cada objeto de Cola tiene los siguientes métodos / funciones:

    # 1. AGREGAR un elemento al FINAL de la cola
    def encolar(self, elemento):
        self.cola.append(elemento)

    # 2. ELIMINAR un elemento al INICIO de la cola
    def desencolar(self):
        if len(self.cola) > 0:
            return self.cola.pop(0)  # la clave es que el PRIMER ELEMENTO SE ELIMINA --> pop(0) --> desencola el primer elemento
        return "No hay elementos en la cola"
    
    # 3. CONSULTAR el primer elemento de la cola, el siguiente en ser eliminado
    def consultar(self):
        if len(self.cola) > 0:
            return self.cola[0]  # muestra el valor al inicio de la cola
        else: 
            return "¡La cola está vacía!"
        

colaReproduccion = Cola()

colaReproduccion.encolar('Un verano sin ti')

colaReproduccion.encolar('Un Coco')

colaReproduccion.encolar('Moscow Mule')
print("Cola inicial: " , colaReproduccion.cola)

print("Siguiente en la cola: " , colaReproduccion.consultar())

colaReproduccion.desencolar()
print("Cola actual: ", colaReproduccion.cola)
