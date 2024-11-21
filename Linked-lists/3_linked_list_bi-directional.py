"""
Lista Doblemente Enlazada (Doubly Linked List)

Una lista doblemente enlazada es una estructura de datos en la que cada nodo tiene dos punteros:
 1. Uno que apunta al siguiente nodo (next_node).
 2. Otro que apunta al nodo anterior (prev_node).
 Esto permite recorrer la lista en ambas direcciones, hacia adelante y hacia atrás.


 Ventajas:
 - Permite una inserción y eliminación eficiente de nodos en cualquier parte de la lista, ya que se puede acceder tanto al nodo anterior como al siguiente.
 - Se puede recorrer la lista tanto de manera ascendente como descendente.

 Desventajas:
 - Mayor uso de memoria, ya que cada nodo debe almacenar dos punteros en lugar de uno.
 - Requiere más operaciones de gestión de punteros para mantener la integridad de la lista (es decir, cuando se agregan o eliminan nodos).

 Usos comunes:
 - Cuando se necesita recorrer la lista en ambas direcciones (por ejemplo, en la implementación de ciertas estructuras como pilas o colas con acceso hacia adelante y atrás).
 - En aplicaciones que requieren operaciones frecuentes de inserción y eliminación en listas de tamaño variable (como en sistemas de gestión de memoria).
"""

# Clase Nodo para una lista doblemente enlazada
# Nota: el nodo de la lista doble enlazada es distinto al nodo de la lista uni-directional (singly linked-list) en el sentido que tiene dos pointers en ves de uno: un pointer al nodo siguiente, y otro al nodo anterior. 
class Dnode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value  # El valor almacenado en el nodo
        self.next_node = next_node  # El siguiente nodo
        self.prev_node = prev_node  # El nodo anterior (atributo clave en listas doblemente enlazadas)

    def set_next_node(self, next_node):
        self.next_node = next_node  # Establece el siguiente nodo
    
    def get_next_node(self):
        return self.next_node  # Obtiene el siguiente nodo
    
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node  # Establece el nodo anterior
    
    def get_prev_node(self):
        return self.prev_node  # Obtiene el nodo anterior
    
    def get_value(self):
        return self.value  # Obtiene el valor del nodo


# Creando la clase para la lista doblemente enlazada
class LinkedList:
    def __init__(self):
        self.head_node = None  # Inicializa la cabeza de la lista como None
        self.tail_node = None  # Inicializa la cola de la lista como None

    def get_head_node(self):
        return self.head_node  # Devuelve el nodo cabeza de la lista
    
    def print_head_node(self):
        print(self.head_node.value)  # Imprime el valor del nodo cabeza
    
    def print_tail_node(self):
        print(self.tail_node.value)  # Imprime el valor del nodo cola

    def add_to_head(self, new_value):
        """
        Recibe un valor y lo agrega al inicio de la lista enlazada.
        Si ya existe un nodo cabeza, conecta el nuevo nodo con el actual en ambas direcciones.
        """
        new_head = Dnode(new_value)  # Crea un nuevo nodo
        current_head = self.head_node

        if current_head is not None:  # Si hay un nodo cabeza existente, lo conecta con el nuevo nodo
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head  # Actualiza la cabeza de la lista al nuevo nodo

        if self.tail_node is None:  # Si no existe un nodo cola, se establece el nuevo nodo como cola también
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        """
        Recibe un valor y lo agrega al final de la lista enlazada.
        Si ya existe un nodo cola, lo conecta con el nuevo nodo en ambas direcciones.
        """
        new_tail = Dnode(new_value)  # Crea un nuevo nodo
        current_tail = self.tail_node

        if current_tail is not None:  # Si hay un nodo cola existente, lo conecta con el nuevo nodo
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail  # Establece el nuevo nodo como cola de la lista

        if self.head_node is None:  # Si no existe un nodo cabeza, se establece el nuevo nodo como cabeza también
            self.head_node = new_tail

    def remove_head(self):
        """
        Elimina el nodo cabeza de la lista.
        Si solo hay un nodo, también elimina el nodo cola.
        """
        removed_head = self.head_node

        if removed_head is None:  # Si la lista está vacía, no hace nada
            return None

        self.head_node = removed_head.get_next_node()  # La cabeza ahora es el siguiente nodo

        if self.head_node is not None:
            self.head_node.set_prev_node(None)  # Desconecta el nodo cabeza de la lista

        if removed_head == self.tail_node:  # Si el nodo cabeza también es el nodo cola, se elimina la cola
            self.remove_tail()

        return removed_head.get_value()  # Devuelve el valor del nodo eliminado

    def remove_tail(self):
        """
        Elimina el nodo cola de la lista.
        Si solo hay un nodo, también elimina el nodo cabeza.
        """
        removed_tail = self.tail_node

        if removed_tail is None:  # Si la lista está vacía, no hace nada
            return None

        self.tail_node = removed_tail.get_prev_node()  # La cola ahora es el nodo anterior

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)  # Desconecta el nodo cola de la lista

        if removed_tail == self.head_node:  # Si el nodo cola también es el nodo cabeza, se elimina la cabeza
            self.remove_head()

        return removed_tail.get_value()  # Devuelve el valor del nodo eliminado

    def stringify_list(self):
        """
        Devuelve una representación en cadena de la lista enlazada.
        Recorre la lista desde el nodo cabeza hasta el nodo cola, agregando los valores de cada nodo.
        """
        print("Lista enlazada actual:")
        string_list = ""
        current_node = self.get_head_node()  # Comienza desde el nodo cabeza
        while current_node:  # Mientras haya nodos en la lista
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"  # Agrega el valor del nodo a la cadena
            current_node = current_node.get_next_node()  # Se mueve al siguiente nodo
        return string_list


if __name__ == "__main__":
    print("")
    double_linked_list = LinkedList()  # Crea una lista doblemente enlazada
    print("Se ha creado el nodo cabeza.")
    double_linked_list.add_to_head("20")  # Agrega un nodo con valor '20' al inicio
    double_linked_list.print_head_node()  # Imprime el valor del nodo cabeza
    print("Se ha agregado el nodo cola:")
    double_linked_list.add_to_tail('24')  # Agrega un nodo con valor '24' al final
    double_linked_list.print_tail_node()  # Imprime el valor del nodo cola
    print("Nuevo nodo cabeza es '18'")
    double_linked_list.add_to_head('18')  # Agrega un nodo con valor '18' al inicio
    print(double_linked_list.stringify_list())  # Imprime toda la lista
    print("'24' es eliminado como nodo cola")
    double_linked_list.remove_tail()  # Elimina el nodo cola
    print(double_linked_list.stringify_list())  # Imprime la lista después de eliminar el nodo cola