

"""
3, 5, 8, 4, 5 

delete node_8

node_8.next = node_4

"""
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.leftChild = left
        self.rightChild = right

class BinaryTree:
    def __init__(self):
        # when binary tree is created, sgtart with an empty root node 
        self.root = None 


    def search(self, value, starting_node=None):
        """
        Search function in Binary Tree. 
        Inputs: value to search for & node to start search in (optional)
        """
        # case where tree is empty 
        if self.root is None:
            return None
        
        # If no starting node is provided, set root node as the starting_node 
        if starting_node is None: 
            starting_node = self.root

        # Check if the current node's value is == data 
        if starting_node.data == value:
            return starting_node
        
        # If value to find is smaller than the current node, search again starting form  left child
        if value < starting_node.data:
            self.search(value, starting_node.leftChild)

        # If value to find is greater than the current node, search again from right Child 
        else:
            self.search(value, starting_node.rightChild)

            

    def insert(self, value, node=None):
        """
        Insertion in a binary tree takes O(logn) time. 
        - insertion in a binary tree is faster than in a 
        - 
        """
        if self.root is None:  # if tree is empty
            self.root = TreeNode(value)  # add the new value as the trees root node 
            return
        
        # if no Node is provided, start iterating from root node
        if node is None:  
            node = self.root
        
        if value < node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)  # insert value here 
            else:
                self.insert(value, node.leftChild) # recursive call on insert, on left child 
        
        elif value > node.value:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
            else:
                self.insert(value, node.rightChild)


        