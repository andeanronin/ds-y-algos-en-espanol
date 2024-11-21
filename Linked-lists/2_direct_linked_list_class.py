
# Estructura de nodos para una lista enlazada simple.

"""
Una lista enlazada (Linked List) es una estructura de datos lineal que consiste en nodos enlazados de forma secuencial. 
Cada nodo contiene dos partes:
1. Un valor almacenado (dato del nodo).
2. Un puntero (o referencia) al siguiente nodo en la lista.

Ventajas:
- Inserciones y eliminaciones rápidas en comparación con los arrays.
- Puede crecer dinámicamente sin necesidad de reservar espacio adicional.

Desventajas:
- Acceso más lento a elementos específicos, ya que requiere recorrer la lista.
- Requiere memoria adicional para almacenar referencias.

Se utiliza en implementaciones de pilas, colas y grafos, entre otros.
"""

# Clase Nodo para construir una lista enlazada.
class Nodo:
    def __init__(self, valor, nodo_siguiente=None):
        self.valor = valor
        self.nodo_siguiente = nodo_siguiente  # contiene solo una referencia al siguiente nodo
    
    def establecer_nodo_siguiente(self, nodo_siguiente):
        self.nodo_siguiente = nodo_siguiente
    
    def obtener_nodo_siguiente(self):
        return self.nodo_siguiente
    
    def obtener_valor(self):
        return self.valor


# Clase ListaEnlazada para crear listas enlazadas.
class ListaEnlazada:
    def __init__(self, valor=None):
        self.nodo_cabeza = Nodo(valor)

    def obtener_nodo_cabeza(self):
        return self.nodo_cabeza  # devuelve el objeto nodo_cabeza
    
    def imprimir_nodo_cabeza(self):
        print(self.nodo_cabeza.valor)  # imprime el valor del nodo_cabeza

    def insertar_al_inicio(self, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)  # crea un nuevo nodo llamado nuevo_nodo
        nuevo_nodo.establecer_nodo_siguiente(self.nodo_cabeza)  # conecta el nuevo nodo al nodo_cabeza actual
        self.nodo_cabeza = nuevo_nodo  # actualiza nodo_cabeza para que apunte al nuevo nodo

    def insertar_al_final(self, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)  # crea un nuevo nodo basado en el valor proporcionado
        if self.nodo_cabeza is None:  # si la lista está vacía, el nuevo nodo se convierte en nodo_cabeza
            self.nodo_cabeza = nuevo_nodo
            return
        nodo_actual = self.nodo_cabeza  # comienza a recorrer desde nodo_cabeza
        while nodo_actual.nodo_siguiente:
            nodo_actual = nodo_actual.nodo_siguiente  # avanza hasta el último nodo
        nodo_actual.nodo_siguiente = nuevo_nodo  # establece el nuevo nodo como el siguiente del último nodo

    def lista_a_cadena(self):
        print("Lista enlazada actual:")
        cadena = ""
        nodo_actual = self.obtener_nodo_cabeza()  # comienza desde nodo_cabeza
        while nodo_actual:  # recorre la lista
            if nodo_actual.obtener_valor() is not None:
                cadena += str(nodo_actual.obtener_valor()) + "\n"  # agrega el valor actual a la cadena
            nodo_actual = nodo_actual.obtener_nodo_siguiente()  # avanza al siguiente nodo
        return cadena

    def eliminar_nodo(self, valor_a_eliminar):
        nodo_actual = self.obtener_nodo_cabeza()
        if nodo_actual.obtener_valor() == valor_a_eliminar:
            self.nodo_cabeza = nodo_actual.obtener_nodo_siguiente()
        else:
            while nodo_actual:
                nodo_siguiente = nodo_actual.obtener_nodo_siguiente()
                if nodo_siguiente.obtener_valor() == valor_a_eliminar:
                    nodo_actual.establecer_nodo_siguiente(nodo_siguiente.obtener_nodo_siguiente())
                    nodo_actual = None
                else:
                    nodo_actual = nodo_siguiente


if __name__ == "__main__":
    # Crear una lista enlazada con un nodo cabeza llamado 'primer nodo'
    una_lista_enlazada = ListaEnlazada("primer nodo")
    una_lista_enlazada.imprimir_nodo_cabeza()  # Imprime el valor del nodo cabeza

    # Inserta un nuevo nodo al inicio
    una_lista_enlazada.insertar_al_inicio('segundo nodo')
    una_lista_enlazada.imprimir_nodo_cabeza()  # Imprime el valor del nodo cabeza

    # Imprime los valores de los nodos en formato de cadena
    print(una_lista_enlazada.lista_a_cadena())

    # Agrega un nuevo nodo
    una_lista_enlazada.insertar_al_inicio('nodo para eliminar')
    print(una_lista_enlazada.lista_a_cadena())

    # Elimina un nodo
    una_lista_enlazada.eliminar_nodo('nodo para eliminar')
    print(una_lista_enlazada.lista_a_cadena())

    # Agrega un nodo al final
    una_lista_enlazada.insertar_al_final('insertado al final')
    print(una_lista_enlazada.lista_a_cadena())