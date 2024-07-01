class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):  # 
    # creates parent-child relationship
    print("Adding " + child_node.value) # The child_node must be a TreeNode object, so that it contains a value param
    self.children.append(child_node) 
  
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

if __name__ == "__main__":
  a_tree_node = TreeNode('I am the root of a tree!') # Creates root node

  # Creating the other 2 nodes that will later be added as children of the tree node
  child_node_1 = TreeNode('I am the child node, a branch of the tree!')
  child_node_2 = TreeNode("I am another child node, a different branch of the tree")

  # Adding the child nodes as children of the tree node. 
  a_tree_node.add_child(child_node_1)
  a_tree_node.add_child(child_node_2)

  # Printing the value of the tree node object 
  print(a_tree_node.value)
  print(a_tree_node.children)
