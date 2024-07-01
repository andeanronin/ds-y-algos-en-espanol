
# Binary Tree Class:
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

# Node Insertion Method 
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data

# Print the Tree
   def PrintTree(self):
      if self.left:     # if there is a node to the left of the current node, 
         self.left.PrintTree()  # go to that node, recur
      print(self.data),  # prints node when there is no node to the left 
      if self.right:     # 
         self.right.PrintTree()
        
# Inorder traversal function: Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
   
if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    # prints the root object, which is a tree with 27 as its root node and 14 and 35 as its left and right nodes respectively:
    root.PrintTree()  
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.inorderTraversal(root))  