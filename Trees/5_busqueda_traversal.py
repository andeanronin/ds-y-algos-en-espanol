"""
Descripción:

Este es un ejemplo de un árbol binario de búsqueda. Cada nodo en el árbol tiene un valor y dos posibles nodos hijos (izquierdo y derecho). Los nodos en el subárbol izquierdo tienen valores menores que el nodo raíz, y los nodos en el subárbol derecho tienen valores mayores que el nodo raíz.

**Recorrido Inorden**: El recorrido inorden sigue el patrón: izquierda -> raíz -> derecha. Este recorrido es útil porque, en un árbol binario de búsqueda, da como resultado una lista de los valores de los nodos en orden ascendente.
"""

# Clase del Árbol Binario:
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Método de inserción de nodos:
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Imprimir el Árbol
    def PrintTree(self):
        if self.left:  # Si hay un nodo a la izquierda del nodo actual,
            self.left.PrintTree()  # ir a ese nodo y realizar la llamada recursiva
        print(self.data),  # Imprime el valor del nodo cuando no hay un nodo a la izquierda
        if self.right:  # Si hay un nodo a la derecha
            self.right.PrintTree()  # Realiza la llamada recursiva al nodo derecho
        
    # Función de recorrido Inorden: Izquierda -> Raíz -> Derecha
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)  # Recorrido recursivo por la izquierda
            res.append(root.data)  # Agrega el nodo raíz a la lista de resultados
            res = res + self.inorderTraversal(root.right)  # Recorrido recursivo por la derecha
        return res

if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    # Imprime el árbol con 27 como el nodo raíz, y 14 y 35 como sus nodos hijos izquierdo y derecho respectivamente:
    root.PrintTree()
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.inorderTraversal(root))  # Imprime el recorrido inorden de los nodos del árbol