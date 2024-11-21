""" 
La cola (Queue) es una estructura de datos similar al array o la lista de python, pero con una serie de reglas mas rigidas.
Reglas:
   1. Nuevos datos agregan datos al final (enque)
   2. Solo se pueden eliminar datos desde el inico de la cola (deque)
   3. FIFO (first in first out) --> el primer dato en entrar al Q (cola) es el primero en irse

Por ende, la "clase" para la estructura de cola tiene tres métodos:
    # 1. Agregar al final de la lista (Enqueue)
    # 2. Eliminar desde el inicio de la lista (Dequeue)
    # 3. Peek: devuelve el valor del nodo al inicio de la cola
"""
class Queue:
   def __init__(self):
      self.queue = list()

    # Metodo para insertar elemento/dato alfinal del Q / cola
   def enqueue(self,dataval):
    if dataval not in self.queue:
        self.queue.insert(0,dataval)
        return True
    return False

    # Metodo para remover elmento de la cola. 
   def dequeue(self):
      if len(self.queue)>0:
         return self.queue.pop()
      return ("No elements in Queue!")

   def peek_q(self):
      print(self.queue[-1])

   def print_q(self):
      print(self.queue)

   def size(self):
      return len(self.queue)

if __name__ == "__main__":
    TheQueue = Queue()
    TheQueue.enqueue("Mon")
    TheQueue.enqueue("Tue")
    TheQueue.enqueue("Wed")  
    TheQueue.print_q()
    TheQueue.peek_q()
    TheQueue.dequeue()
    TheQueue.print_q()
    TheQueue.peek_q()   # not working right