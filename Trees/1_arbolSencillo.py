"""
Descripción de la Estructura de Datos Árbol:
Un árbol es una estructura de datos jerárquica que consiste en nodos conectados entre sí. Cada árbol tiene un nodo raíz (raíz) y nodos hijos que forman ramas. 
En un árbol binario, cada nodo tiene como máximo dos hijos: hijo izquierdo y hijo derecho.

Ventajas:
- Los árboles permiten almacenar datos de manera jerárquica y eficiente.
- Son ideales para representar estructuras jerárquicas, como sistemas de archivos o árboles de decisiones.
- Las operaciones de búsqueda, inserción y eliminación en un árbol binario equilibrado tienen un tiempo de ejecución eficiente de O(log n).

Desventajas:
- Si el árbol no está balanceado, las operaciones pueden degenerar en una lista enlazada, lo que reduce su eficiencia a O(n).
- La implementación de árboles es más compleja que otras estructuras de datos lineales, como listas o pilas.

Casos de uso:
- Los árboles binarios de búsqueda (BST) se utilizan para realizar búsquedas rápidas de datos.
- Los árboles AVL o Red-Black Trees se usan cuando se necesita garantizar que el árbol se mantenga equilibrado.
- Los árboles son ampliamente utilizados en la representación de datos jerárquicos como las bases de datos, árboles de expresiones y árboles de decisión.
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data  # Dato almacenado en el nodo
        self.leftChild = left  # Hijo izquierdo del nodo
        self.rightChild = right  # Hijo derecho del nodo

class BinaryTree:
    def __init__(self):
        # Cuando se crea el árbol binario, comienza con un nodo raíz vacío
        self.root = None

    def search(self, value, starting_node=None):
        """
        Función de búsqueda en un árbol binario.
        Entradas: valor a buscar y nodo de inicio (opcional).
        """
        # Caso en el que el árbol está vacío
        if self.root is None:
            return None
        
        # Si no se proporciona un nodo de inicio, se establece el nodo raíz como el nodo de inicio
        if starting_node is None: 
            starting_node = self.root

        # Verifica si el valor del nodo actual es igual al dato buscado
        if starting_node.data == value:
            return starting_node
        
        # Si el valor buscado es menor que el nodo actual, busca en el hijo izquierdo
        if value < starting_node.data:
            return self.search(value, starting_node.leftChild)

        # Si el valor buscado es mayor que el nodo actual, busca en el hijo derecho
        else:
            return self.search(value, starting_node.rightChild)

    def insert(self, value, node=None):
        """
        Inserción en un árbol binario. Toma O(logn) tiempo.
        La inserción en un árbol binario es más rápida que en una lista enlazada.
        """
        if self.root is None:  # Si el árbol está vacío
            self.root = TreeNode(value)  # Agrega el nuevo valor como el nodo raíz del árbol
            return
        
        # Si no se proporciona un nodo, comienza desde el nodo raíz
        if node is None:  
            node = self.root
        
        if value < node.data:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)  # Inserta el valor en el hijo izquierdo
            else:
                self.insert(value, node.leftChild)  # Llamada recursiva para insertar en el hijo izquierdo
        
        elif value > node.data:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)  # Inserta el valor en el hijo derecho
            else:
                self.insert(value, node.rightChild)  # Llamada recursiva para insertar en el hijo derecho

    def in_order_traversal_and_print(self, node=None):
        """
        Recorre el árbol en el siguiente orden: izquierdo -> raíz -> derecho
        """
        if node is None:
            node = self.root  # Si no se proporciona un nodo, comienza desde el nodo raíz

        if node:  # Si el nodo existe (no es None)
            self.in_order_traversal_and_print(node.leftChild)  # Recorre el hijo izquierdo
            print(node.data)  # Imprime el dato del nodo actual
            self.in_order_traversal_and_print(node.rightChild)  # Recorre el hijo derecho

    def pre_order_traversal(self, node=None):
        """
        Recorre el árbol en el siguiente orden: raíz -> izquierdo -> derecho
        """
        if node is None:
            node = self.root
        
        if node:
            print(node.data)  # Imprime el dato del nodo actual
            self.pre_order_traversal(node.leftChild)  # Recorre el hijo izquierdo
            self.pre_order_traversal(node.rightChild)  # Recorre el hijo derecho