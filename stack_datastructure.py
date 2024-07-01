
# Defining a Stack Data Structure 
class Stack(object):
    def __init__( self):
        self.stack = []                  # Stack is a stores stuff in a list data structure
    def get_stack_elements(self):
        return self.stack.copy()        
    def add_item(self , item):
        self.stack.append(item)
    def add_many(self , item, n):
        for i in range(n):
            self.stack.append(item)
    def remove_item(self):
        self.stack.pop()
    def remove_many(self , n):
        for i in range(n):
            self.stack.pop()
    def size(self):
        return len(self.stack)
    def prettyprint(self):
        for item in self.stack[::-1]:
            print('|_',item, '_|')



if __name__ == '__main__':
    # Creating a pancakes object, which is an instance of the Stack class
    pancakes = Stack()

    # Using methods of the stack class:
    pancakes.add_item('blueberry slice')
    pancakes.add_many('chocolatte',4)
    pancakes.prettyprint()
    print("")
    pancakes.remove_item()
    print("After eating top pancake:")
    pancakes.prettyprint()