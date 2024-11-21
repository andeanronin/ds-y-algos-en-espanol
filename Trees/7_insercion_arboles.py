"""
Descripción:

Este script crea un árbol binario de búsqueda. En un árbol binario de búsqueda, los nodos a la izquierda de un nodo tienen valores menores, y los nodos a la derecha tienen valores mayores.

**Inserción de Nodos**: El método `insert` agrega un nuevo nodo al árbol de acuerdo con el valor proporcionado. Si el valor es menor que el nodo actual, el nodo se agrega en el subárbol izquierdo; si es mayor, se agrega en el subárbol derecho. Si no hay espacio en el lado correspondiente, el nodo se agrega allí.
"""

# Clase de Árbol Binario
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  # Método de Inserción de Nodos
  def insert(self, data):
    if self.data:
      if data < self.data:  # Si el dato es menor que el nodo padre
        if self.left is None: # Si no hay valor a la izquierda del nodo padre
          self.left = Node(data)   # Se agrega al lado izquierdo del nodo padre
        else:
          self.left.insert(data)  # Recursivamente se inserta en el subárbol izquierdo
      elif data > self.data:   # Si el dato es mayor que el nodo padre
        if self.right is None:
          self.right = Node(data)  # Se agrega al lado derecho del nodo padre
        else:
          self.right.insert(data)  # Recursivamente se inserta en el subárbol derecho
    else:
      self.data = data

  # Imprimir el árbol
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.data),  # Imprime el valor del nodo
    if self.right:
      self.right.PrintTree()

# Usar el método insert para agregar nodos
if __name__ == "__main__":
  root = Node(12)
  root.insert(6)
  root.insert(14)
  root.insert(3)
  root.PrintTree()  # Imprime el árbol después de insertar los nodos