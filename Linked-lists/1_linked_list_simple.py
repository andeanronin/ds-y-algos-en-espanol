# Nodo y lista enlazada simple.

"""
Una lista enlazada simple es una estructura de datos lineal en la que cada elemento (nodo) apunta al siguiente nodo en la secuencia.
Cada nodo contiene dos componentes:
1. `data`: el valor almacenado en el nodo.
2. `next`: una referencia al siguiente nodo en la lista.

Ventajas:
- Es eficiente en la inserción y eliminación de elementos en comparación con arrays.
- Crece dinámicamente según sea necesario.

Desventajas:
- El acceso a elementos específicos es lento, ya que requiere recorrer la lista.
- Consume más memoria debido al almacenamiento de referencias adicionales.
"""

# Clase SimpleNode para crear nodos individuales en la lista enlazada.
class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Clase SimpleLinkedList para implementar una lista enlazada simple.
class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None
    
    # Agregar un nodo nuevo al final de la lista.
    def append(self, dato):
        nuevo_nodo = NodoSimple(dato)

        # Caso 1: la lista está vacía, el nuevo nodo se convierte en la cabeza.
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return  # El nuevo nodo se agrega como cabeza, termina la función.
        
        # Caso 2: la lista tiene un nodo cabeza.
        # Recorremos la lista hasta llegar al último nodo y establecemos su `siguiente` al nuevo nodo.
        ultimo = self.cabeza
        while ultimo.siguiente:  # Mientras exista un nodo siguiente, seguimos recorriendo.
            ultimo = ultimo.siguiente  # Saltamos al siguiente nodo.

        ultimo.siguiente = nuevo_nodo  # Establecemos el siguiente del último nodo como el nuevo nodo.

    # Agregar un nodo nuevo al principio de la lista.
    def prepend(self, dato):
        nuevo_nodo = NodoSimple(dato)

        if not self.cabeza:  # Si la lista está vacía, el nuevo nodo se convierte en la cabeza.
            self.cabeza = nuevo_nodo
            return

        nuevo_nodo.siguiente = self.cabeza  # El nuevo nodo apunta al nodo cabeza actual.

        self.cabeza = nuevo_nodo  # El nuevo nodo se convierte en la nueva cabeza.

    # Eliminar un valor dado de la lista enlazada.
    def eliminar(self, dato):
        """
        Pasos:
        1. Iterar sobre la lista enlazada hasta encontrar el nodo con el dato.
        2. Saltar el nodo actual para eliminarlo de la lista.
        3. Actualizar el valor `siguiente` del nodo previo para que apunte al nodo posterior al nodo actual.
        """
        if not self.cabeza:  # Salir de la función si la lista está vacía.
            return 
        
        if self.cabeza.dato == dato:  # Caso: el dato a eliminar está en la cabeza.
            self.cabeza = self.cabeza.siguiente
            return 
        
        nodo_previo = None
        nodo_actual = self.cabeza
        while nodo_actual and nodo_actual.dato != dato:  # Recorrer la lista buscando el dato a eliminar.
            nodo_previo = nodo_actual
            nodo_actual = nodo_actual.siguiente  # Saltar al siguiente nodo en cada iteración.

        if nodo_actual is None:
            return  # Si no se encuentra el dato, salir de la función.

        # El nodo actual contiene el dato a eliminar, lo saltamos en la lista.
        nodo_previo.siguiente = nodo_actual.siguiente