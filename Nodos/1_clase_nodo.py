"""
Resumen sobre la clase nodo:

¿Qué es una clase Node?
Una clase Node en Python es un bloque fundamental para la implementación de listas enlazadas. Una lista enlazada es una estructura de datos lineal donde cada elemento (nodo) apunta al siguiente elemento de la lista. La clase Node generalmente contiene dos partes: un valor que guarda la información y una referencia al siguiente nodo. Esta estructura es útil para manejar datos de manera dinámica, ya que los nodos pueden ser agregados o eliminados sin reorganizar todo el conjunto de datos.

¿Cuándo se usa?
Se utiliza en la implementación de listas enlazadas, pilas, colas y otras estructuras de datos donde el acceso secuencial y la inserción/eliminación de elementos en tiempo constante son importantes.

Pros y Contras de las listas enlazadas:

Pros:
- Permite insertar y eliminar elementos de manera eficiente.
- No requiere un tamaño fijo de memoria, lo que lo hace adecuado para situaciones donde el tamaño de los datos cambia frecuentemente.

Contras:
- El acceso a elementos es secuencial, lo que puede hacer que la búsqueda de un valor sea más lenta que en otras estructuras como arreglos.
- Consume más memoria debido a las referencias adicionales entre nodos.

Este enfoque es ideal para implementar estructuras de datos dinámicas como listas y pilas, pero no es tan eficiente para accesos aleatorios a elementos.
"""

# Nodo simple en Python para listas enlazadas, contiene dos variables de instancia: valor y siguiente nodo 
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
  


if __name__ == "__main__":
    first_node = Node(14)           # Crear un Nodo, obtener su valor y crear su siguiente nodo
    print(first_node.get_value())   # Obtener el valor retorna el valor del nodo actual 

    second_node = first_node.set_next_node(30)   # Establece el siguiente nodo como 30
    print(first_node.get_next_node())   # El primer nodo ahora tiene su propio valor Y el valor del siguiente nodo
    print("")

    disconected_node = Node('hello')
    print(disconected_node.get_next_node())   # Aún no tiene siguiente nodo, por lo que imprime NONE