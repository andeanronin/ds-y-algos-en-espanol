
# Simple Python Node for Linked Lists, contains two instance variables: value & next node 
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
  


if __name__ == "__main__":
    first_node = Node(14)           # Create a Node, get its value, and create its next node
    print(first_node.get_value())   # Get value returns value of current node 

    second_node = first_node.set_next_node(30)   # sets the next node to 30
    print(first_node.get_next_node())   # the first node now has its own value AND the next node's value
    print("")

    disconected_node = Node('hello')
    print(disconected_node.get_next_node())   # No next node yet, so prints NONE 
