"""
Descripción:

Este es un ejemplo de un árbol binario de búsqueda, donde cada nodo tiene un valor y dos hijos (izquierdo y derecho). En un árbol binario de búsqueda, todos los nodos en el subárbol izquierdo de un nodo tienen valores menores, y todos los nodos en el subárbol derecho tienen valores mayores.

**Recorrido Preorden**: El recorrido preorden sigue el patrón: raíz -> izquierda -> derecha. En este recorrido, se visita primero el nodo raíz, luego se recurre al subárbol izquierdo y finalmente al subárbol derecho.
"""

# Clase del Árbol Binario:
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   # Insertar Nodo
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
      if self.left:
         self.left.PrintTree()
      print(self.data),
      if self.right:
         self.right.PrintTree()

   # Recorrido Preorden: Raíz -> Izquierda -> Derecha
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)  # Primero, se agrega la raíz
         res = res + self.PreorderTraversal(root.left)  # Luego, se recorre el subárbol izquierdo
         res = res + self.PreorderTraversal(root.right)  # Finalmente, se recorre el subárbol derecho
      return res

if __name__ == "__main__":
   root = Node(27)
   root.insert(14)
   root.insert(35)
   root.insert(10)
   root.insert(19)
   root.insert(31)
   root.insert(42)
   print(root.PreorderTraversal(root))  # Imprime el recorrido preorden de los nodos del árbol