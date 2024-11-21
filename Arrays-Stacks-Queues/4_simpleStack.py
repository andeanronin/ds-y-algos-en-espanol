# Torre Simple (Simple Stack)

# Una torre (Stack) es una estructura de datos lineal que sigue el principio LIFO (Last In, First Out), 
# es decir, el último elemento en entrar es el primero en salir. 
# Se utiliza comúnmente para tareas donde se requiere rastrear o deshacer acciones en orden inverso, 
# como un historial de navegación o el manejo de operaciones en un editor de texto.

"""
1. Almacenar valores en un array
2. Insertar valores en la CIMA de la torre
3. Eliminar valores desde la CIMA de la torre
"""

class TorreSimple(object):
    # todas las instancias de torre se inicializan con un array / lista vacío
    def __init__(self):  
        self.torre = []   # self es la instancia específica, torre es su variable que almacena el array 
    
    # las torres deben tener un método para agregar elementos en la cima
    def push(self, elemento):
        self.torre.append(elemento)

    # las torres deben tener un método para eliminar el elemento en la cima
    def remove(self):
        self.torre.pop()

    # imprimir torre
    def imprimirBonito(self):
        for elemento in self.torre[::-1]:
             print('|_', elemento, '_|')



if __name__ == "__main__":
    # crear una torre de ejemplo:
    print("Inicio")

    panqueque = TorreSimple()  # panqueque es un objeto de la clase TorreSimple

    panqueque.push('crepe de arándanos') 
    print(panqueque)  # esto imprime el OBJETO TorreSimple

    panqueque.push('crepe de chocolate')
    print(panqueque.torre)  # esto imprime la torre actual 

    panqueque.push('crepe de miel')
    panqueque.imprimirBonito()  # usa el método imprimirBonito de la clase TorreSimple

    print('')
    panqueque.remove()
    panqueque.imprimirBonito()

