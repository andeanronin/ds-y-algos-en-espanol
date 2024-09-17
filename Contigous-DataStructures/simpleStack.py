# Simple Stack

"""
1. Store values in an array
2. Insert values at the TOP of the stack
3. Remove values at the TOP of the stack
"""

class SimpleStack(object):
    # all stack instances are initialized with an empty array / list
    def __init__(self):  
        self.stack = []   # self is the specific instance, stack is its variable that stores the array 
    
    # stacks must have a method to push items at the top
    def push(self, item):
        self.stack.append(item)

    # stacks must have a method to remove the item at the top of the stack
    def remove(self):
        self.stack.pop()

    # print stack
    def prettyPrint(self):
        for item in self.stack[::-1]:
             print('|_',item,'_|')



if __name__ == "__main__":
    # create an example stack:
    print("start")

    pancake = SimpleStack() # pancake is an object with a SimpleStack class

    pancake.push('blueberry crepe') 
    print(pancake)  # this prints out the simpleStack OBJECT 

    pancake.push('chocolate crepe')
    print(pancake.stack)  # this prints out the actual stack 

    pancake.push('honey crepe')
    pancake.prettyPrint() # this uses the pretty print method of the simpleStack class

    print('')
    pancake.remove()
    pancake.prettyPrint()


