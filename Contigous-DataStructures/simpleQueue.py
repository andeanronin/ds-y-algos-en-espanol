# Simple Queue Class

class Queue:
    def __init__(self): 
        self.queue = list()   # every queue object is initialized with an empty list / array

    # Every Queue object has the following methods / functions: 

    # 1. ADD item at the END of the line / queue 
    def enqueue(self, item):
        self.queue.append(item)

    # 2. REMOVE item at the start of the line / queue 
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)   # key here is that the FIRST ITEM IS REMOVED -->  pop(0)  --> dequeues first item 
        return "No elements in Queue"
    
    # 3. PEEK at the first element in the queue, next value to be removed 
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]  # prints the value at the end of the queue
        else: 
            return "Queue is empty!!"
        

playListQueue = Queue()

playListQueue.enqueue('Bitch As Niggaz')

playListQueue.enqueue('Niggaz in Paris')

playListQueue.enqueue('Straight Outta Compton')
print("Starting Queue: " , playListQueue.queue)

print("Next in Line: " , playListQueue.peek())

playListQueue.dequeue()
print("Current Queue: ", playListQueue.queue)

