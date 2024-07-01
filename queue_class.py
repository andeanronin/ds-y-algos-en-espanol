# The Queue in python is a data strucutre whose instance variable is a list
# The Queue data class has three methods:
    # 1. Add to the end of list Enqueue
    # 2. Remove from the beginning of list Dequeue
    # 3. Peek: returns value of node at the beginning of the queue

class Queue:
   def __init__(self):
      self.queue = list()

    # Insert method to add element to start of Q
   def enqueue(self,dataval):
    if dataval not in self.queue:
        self.queue.insert(0,dataval)
        return True
    return False

    # Method to remove element from Q 
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