"""
Descripción del Nodo de un Árbol Binario:
Un nodo en un árbol binario es una unidad fundamental que contiene tres elementos: 
1. Un valor (dato) almacenado en el nodo.
2. Un puntero (referencia) al hijo izquierdo.
3. Un puntero (referencia) al hijo derecho.
El nodo se utiliza para representar la estructura jerárquica del árbol, donde cada nodo puede tener como máximo dos hijos: uno a la izquierda y otro a la derecha. 
El nodo raíz es el nodo inicial de un árbol binario y sirve como punto de partida para todas las operaciones de búsqueda, inserción y recorrido en el árbol.

El rol del nodo en un árbol binario es almacenar los datos y proporcionar las conexiones entre nodos a través de los punteros de los hijos izquierdo y derecho, permitiendo una estructura de datos jerárquica eficiente.
"""

class Node:
    def __init__(self, key):
        self.left = None  # Hijo izquierdo del nodo
        self.right = None  # Hijo derecho del nodo
        self.val = key  # Valor almacenado en el nodo

# Implementando un Árbol Binario
if __name__ == '__main__':
    # Crear la raíz
    root = Node(1)
    ''' Lo siguiente es el árbol después de la declaración anterior:
    1
    / \
    None None '''
    root.left = Node(2)
    root.right = Node(3)
 
    ''' 2 y 3 se convierten en los hijos izquierdo y derecho de 1:
       1
      /  \
     2    3
    / \  / \
   None None None None'''
 
    root.left.left = Node(4)
    ''' 4 se convierte en el hijo izquierdo de 2:
        1
       / \
      2   3
     / \ / \
    4 None None None
   / \
   None None'''