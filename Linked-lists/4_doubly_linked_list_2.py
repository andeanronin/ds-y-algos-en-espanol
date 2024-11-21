class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None # node can be initialized without next value
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        """
        Append data to the end of the linked list
        1. Initialize data to be appended as a Node() object type
        2. Linked list is empty
        3. Linked list is not empty: go to last node, set it's next.node = new_node
        """
        # 1. Initialize data as node
        new_node = DoubleNode(data)

        # 2. When linked-list is emtpy
        if not self.head: # if there is is no head node
            self.head = new_node
            return

        # 3. Start at head.node, and iterate over the list until you reach the last node --> last.node.next == None
        Last_node = self.head
        while Last_node.next:  # stops when Last_node.next == None
            Last_node = Last_node.next

        # Place the new node at the end of list 
        Last_node.next = new_node

        # link new node to the previous node in the doubly linked list
        new_node.prev = Last_node


    def PrePend(self, data):
        """
        Add data to beginning of the list
        1. Initialize the data as a node
        2. If list is empty, set new_node = self.head
        """
        new_node = DoubleNode(data)

        if not self.head:
            self.head = new_node

        new_node.next = self.head  # insert new node to beginning of the list
        self.head.prev = new_node  # double connection
        self.head = new_node  # set new_node as the head node


    def delete(self, data):
        """
        Delete a node from a doubly linked list
        1. If linked list is empty, exit function and return nothing
        2. Iterate over linked list until you find the node connecting the data, once the node is found, change the next link of the previous node and the previous link of its next node
            2.1 Handle case when no match is found
            2.2 Handle cases when node to delete is Head
            2.3 Handle cases when node is not head nor last
        """
        # 1. List is empty, nothing to delete 
        if not self.head:
            return 
    
        # 2. Loop over linked list, on each iteration, check if there is a match. If there is a match or if we reach the end of the list (Current = None), exit loop
        Current = self.head
        while Current and Current.data != data:  
            Current = Current.next 
        
        # 2.1 We iterated to the end of the list and no match was found
        if Current == None:
            return
        
        # 2.2 Node to be deleted is the Head Node
        if Current == self.head:
            self.head = Current.next
            if self.head:
                self.head.prev = None
            return
        
        # 2.3 Node is not head nor last
        if Current.next != None:  # there is a node after, so we have to update its Next.Prev value 
            Current.prev.next = Current.next # the prev's node's next pointer must skipp current (must point to current.next )
            Current.next.prev = Current.prev   # The next node's prev pointer must skip the node to delete (ie, must point to current.prev)
        
        # 2.4 Node to delete is the last node
        else: 
            Current.prev.next = None 

    def printLinkedList(self):
        Current = self.head

        while Current != None: 
            print(Current.data) 
            Current = Current.next 
        

if __name__ == "__main__":
    names = DoublyLinkedList()

    names.append("Juan")

    names.append("Diego")

    print("Head Node: ", names.head.data) 

    names.PrePend("Mariano")

    print("New Head Node: ", names.head.data)

    print(names.printLinkedList())
    print("")

    names.PrePend("Nico")

    names.delete("Juan")
    print("After Deleting Juan: ")
    print(names.printLinkedList())

    print("")
    print("After deleting Nico")
    names.delete("Nico")
    print(names.printLinkedList())

    




        
        





