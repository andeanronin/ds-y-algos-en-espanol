# Definiendo una Estructura de Datos Torre 
class Torre(object):
    def __init__(self):
        self.torre = []  # La torre almacena elementos en una estructura de datos tipo lista
    
    def obtener_elementos(self):
        return self.torre.copy()
    
    def agregar_elemento(self, elemento):
        self.torre.append(elemento)
    
    def agregar_varios(self, elemento, n):
        for i in range(n):
            self.torre.append(elemento)
    
    def eliminar_elemento(self):
        self.torre.pop()
    
    def eliminar_varios(self, n):
        for i in range(n):
            self.torre.pop()
    
    def tamano(self):
        return len(self.torre)
    
    def imprimir_bonito(self):
        for elemento in self.torre[::-1]:
            print('|_', elemento, '_|')



if __name__ == '__main__':
    # Creando un objeto panqueques, que es una instancia de la clase Torre
    panqueques = Torre()

    # Usando métodos de la clase Torre:
    panqueques.agregar_elemento('rebanada de arándanos')
    panqueques.agregar_varios('chocolate', 4)
    panqueques.imprimir_bonito()
    print("")
    panqueques.eliminar_elemento()
    print("Después de comer el panqueque de arriba:")
    panqueques.imprimir_bonito()