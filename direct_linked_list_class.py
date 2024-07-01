
# Node structure for a simple linked list. 
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node   # contains only a next-node variable
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value

# Linked-List Class used for Creating Linked-lists 
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node    # returns the head node object
  
  def print_head_node(self):
    print(self.head_node.value)  # prints value of the head node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)   # Creates another Node object called new_node 
    new_node.set_next_node(self.head_node)    # Sets the new_node's next_node value to the previous head_node
    self.head_node = new_node    # re-establishes the linked-list's head-node as the new_node 

  def insert_end(self, new_value):
    new_node = Node(new_value)    # Creates new node based on input
    if self.head_node is None:    # If there are no nodes in list, it sets new_node as the head_node
      self.head_node = new_node   
      return
    iterating_node = self.head_node       # iterates through linked-list 
    while(iterating_node.next_node):
      iterating_node = iterating_node.next_node     # reaches the end of linked list 
    iterating_node.next_node = new_node           # sets the current last node's next_node attirbute = new_node 

  def stringify_list(self):
    print("Current Linked List:")
    string_list = ""
    current_node = self.get_head_node()   # Sets current node to --> head Node
    while current_node:                     # While loop starts from head Node
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"   # Adds the current node's value to the string
      current_node = current_node.get_next_node()       # Sets current node = next node 
    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

if __name__ == "__main__":  
    # Create Linked-list with a head node called 'original node'
    a_linked_list = LinkedList("first node")
    a_linked_list.print_head_node()  # Prints value of head node

    # Inserts new node at the beginning
    a_linked_list.insert_beginning('second node')
    a_linked_list.print_head_node() # Prints value of head node

    # Prints the values of the node in a string format
    print(a_linked_list.stringify_list())

    # Adds new node 
    a_linked_list.insert_beginning('node to delete')
    print(a_linked_list.stringify_list())

    # Removes new node 
    a_linked_list.remove_node('node to delete')
    print(a_linked_list.stringify_list())    

    # Adds node:
    a_linked_list.insert_end('inserted at end')
    print(a_linked_list.stringify_list())