
# Node class for a Doubly Linked-list 
class Dnode:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node     # Nodes in a doubly linked list have a prev_node attribute
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def set_prev_node(self, prev_node):    # Allows you to set the previous value of a node 
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
  
# Creating the Doubly Linked-list Class
class LinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  def get_head_node(self):
    return self.head_node    # returns the head node object
  
  def print_head_node(self):
    print(self.head_node.value)  # prints value of the head node
  
  def print_tail_node(self):
    print(self.tail_node.value)

  def add_to_head(self, new_value):
    """
    Inputs a value, which function adds to the head of the linked list.
    Head_node value of linked-list is updated to = new_value
    If there is already a head_node, the function connects the new_head to the current_head on both directions
    """
    new_head = Dnode(new_value)   # Creates another Node object called new_node 
    current_head = self.head_node

    if current_head != None:    # if there is a current head then connect it with new_head on both ends
      current_head.set_prev_node(new_head)   # connect current head's prev_node value to the new_head
      new_head.set_next_node(current_head)   # connect the new_head's next_node value to the current_head

    self.head_node = new_head # re-establishes the linked-list's head_node value to new_head

    if self.tail_node == None:
      self.tail_node = new_head   # if their is no tail_node then set it its value to the new_head
      
  def add_to_tail(self, new_value):
    new_tail = Dnode(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    
    self.tail_node = new_tail   # Sets list's tail_node attribute to the new_tail 

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)   # disconects current head_node from list

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  def stringify_list(self):
    print("Current Linked List:")
    string_list = ""
    current_node = self.get_head_node()   # Sets current node to --> head Node
    while current_node:                     # While loop starts from head Node
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"   # Adds the current node's value to the string
      current_node = current_node.get_next_node()       # Sets current node = next node 
    return string_list

if __name__ == "__main__":
  print("")
  double_linked_list = LinkedList()
  print("head node is created")
  double_linked_list.add_to_head("20")
  double_linked_list.print_head_node()
  print("tail node is added:")
  double_linked_list.add_to_tail('24')
  double_linked_list.print_tail_node()
  print('New Head node is 18')
  double_linked_list.add_to_head('18')
  print(double_linked_list.stringify_list())
  print("'24' is removed as tail node")
  double_linked_list.remove_tail()
  print(double_linked_list.stringify_list())
