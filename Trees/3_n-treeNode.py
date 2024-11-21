"""
Descripción del Nodo de un Árbol:
Un nodo de árbol es una estructura de datos que representa un elemento dentro de un árbol. 

Cada nodo contiene:
1. Un valor (o dato) almacenado en el nodo.
2. Una lista de referencias a otros nodos, conocidos como sus hijos.

En un árbol, un nodo puede tener varios hijos (en un árbol general) o dos hijos (en un árbol binario). 
El nodo raíz es el nodo principal de un árbol y sirve como punto de partida para recorrer el árbol.
Los nodos pueden tener relaciones de padre a hijo, donde un nodo puede ser el padre de otros nodos, creando una estructura jerárquica.

El rol del nodo es almacenar los datos y las referencias a los nodos hijos, lo que permite organizar los datos en una estructura de árbol que es eficiente para operaciones como la búsqueda, la inserción y el recorrido.
"""

class TreeNode:
  def __init__(self, value):
    self.value = value  # dato almacenado en el nodo
    self.children = []  # referencias a otros nodos (hijos)

  def add_child(self, child_node):  
    # crea una relación padre-hijo
    print("Agregando " + child_node.value)  # El child_node debe ser un objeto TreeNode, para que contenga un parámetro de valor
    self.children.append(child_node)  # añade el hijo al nodo

  def remove_child(self, child_node):
    # elimina la relación padre-hijo
    print("Eliminando " + child_node.value + " de " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]  # filtra el hijo a eliminar

  def traverse(self):
    # recorre cada nodo referenciado desde este nodo hacia abajo
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()  # obtiene el siguiente nodo por visitar
      print(current_node.value)  # imprime el valor del nodo actual
      nodes_to_visit += current_node.children  # añade los hijos del nodo actual a la lista de nodos por visitar

if __name__ == "__main__":
  a_tree_node = TreeNode('¡Soy la raíz de un árbol!')  # Crea el nodo raíz

  # Creando otros 2 nodos que se agregarán más tarde como hijos del nodo raíz
  child_node_1 = TreeNode('¡Soy el nodo hijo, una rama del árbol!')
  child_node_2 = TreeNode("Soy otro nodo hijo, una rama diferente del árbol")

  # Agregando los nodos hijos como hijos del nodo raíz
  a_tree_node.add_child(child_node_1)
  a_tree_node.add_child(child_node_2)

  # Imprimiendo el valor del nodo raíz
  print(a_tree_node.value)
  print(a_tree_node.children)