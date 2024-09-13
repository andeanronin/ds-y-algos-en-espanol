
# Binary Tree Class 
class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def insert(self, data):
    if self.data:
      if data < self.data:  # If input is smaller than parent node
        if self.left is None: # If there is no value to the left of parent node
          self.left = Node(data)   # Add to the left of parent node 
        else:
          self.left.insert(data) 
      elif data > self.data:   # If input is bigger than parent node
        if self.right is None:
          self.right = Node(data) 
        else:
          self.right.insert(data) # Insert to parent node's self.rigth value
    else:
      self.data = data

# Print the tree
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print(self.data),
    if self.right:
      self.right.PrintTree()

# Use the insert method to add nodes
if __name__ == "__main__":
  root = Node(12)
  root.insert(6)
  root.insert(14)
  root.insert(3)
  root.PrintTree()