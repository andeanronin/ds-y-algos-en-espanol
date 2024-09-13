
class Treenode:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


    # In order search  left --> root --> right
    def in_order(self):
        if self == None:     # stops recursion when there is no left node 
            return
        if self.left:
            self.left.in_order() 
        print(self.data)
        if self.right:
            self.right.in_order()

    # DFS (pre-order) root --> left --> right
    def dfs(self):
        if self == None:  # stops recursion when there is no left node
            return
        print(self.data)
        if self.left:
            self.left.dfs()
        if self.right:
            self.right.dfs()
        

    # Post order search   left --> right --> root
    def post_order(self):
        if self == None:
            return
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)
       

if __name__ == "__main__":
    a_simple_tree = Treenode(80)
    a_simple_tree.left = Treenode(20)
    a_simple_tree.right = Treenode(120)
    a_simple_tree.PrintTree()

    print("Pre Order Traversal:")
    a_simple_tree.dfs()

    print("In order traversal:")
    a_simple_tree.in_order()

    print("Post order traversal:")
    a_simple_tree.post_order()
