"""
Descripción de la búsqueda en profundidad (DFS) y recorridos:

La búsqueda en profundidad (DFS) es un algoritmo para recorrer o buscar en un árbol o grafo. Este algoritmo comienza en la raíz y explora tan profundamente como sea posible antes de retroceder.

En un árbol binario, hay tres formas comunes de realizar un recorrido DFS:
1. **Preorden**: El recorrido sigue el patrón: raíz --> izquierda --> derecha.
2. **Inorden**: El recorrido sigue el patrón: izquierda --> raíz --> derecha.
3. **Postorden**: El recorrido sigue el patrón: izquierda --> derecha --> raíz.

El DFS es útil para explorar todos los nodos de un árbol y es especialmente eficiente para árboles con estructuras complejas.
"""

class Treenode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()  # Llamada recursiva al hijo izquierdo
        print(self.data),  # Imprime el dato del nodo actual
        if self.right:
            self.right.PrintTree()  # Llamada recursiva al hijo derecho

    # Búsqueda en orden: izquierda --> raíz --> derecha
    def in_order(self):
        if self == None:  # Detiene la recursión si no hay nodo izquierdo
            return
        if self.left:
            self.left.in_order()  # Llamada recursiva al hijo izquierdo
        print(self.data)  # Imprime el dato del nodo actual
        if self.right:
            self.right.in_order()  # Llamada recursiva al hijo derecho

    # DFS (preorden): raíz --> izquierda --> derecha
    def dfs(self):
        if self == None:  # Detiene la recursión si no hay nodo izquierdo
            return
        print(self.data)  # Imprime el dato del nodo actual
        if self.left:
            self.left.dfs()  # Llamada recursiva al hijo izquierdo
        if self.right:
            self.right.dfs()  # Llamada recursiva al hijo derecho

    # Búsqueda en postorden: izquierda --> derecha --> raíz
    def post_order(self):
        if self == None:  # Detiene la recursión si no hay nodo izquierdo
            return
        if self.left:
            self.left.post_order()  # Llamada recursiva al hijo izquierdo
        if self.right:
            self.right.post_order()  # Llamada recursiva al hijo derecho
        print(self.data)  # Imprime el dato del nodo actual

if __name__ == "__main__":
    a_simple_tree = Treenode(80)
    a_simple_tree.left = Treenode(20)
    a_simple_tree.right = Treenode(120)
    a_simple_tree.PrintTree()  # Imprime el árbol en orden

    print("Recorrido Preorden:")
    a_simple_tree.dfs()  # Recorrido en preorden

    print("Recorrido Inorden:")
    a_simple_tree.in_order()  # Recorrido en inorden

    print("Recorrido Postorden:")
    a_simple_tree.post_order()  # Recorrido en postorden