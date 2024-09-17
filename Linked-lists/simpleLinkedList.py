class SimpleNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:
    def __init__(self):
        self.head = None
    
    # Append a new node to the end of the list 
    def append(self, data):
        new_node = SimpleNode(data) 

        # Case 1: linked list is empty, new data is set to head_node 
        if not self.head:
            self.head = new_node
            return  # new data is added to linked list as its head, function ends 
        
        # Case 2: there is  head node in the linked list
        #  traverse linked list until you reach the last node, then set last node's next.node = new_node
        last = self.head
        while last.next:  # if there is a next node, loop stops when there is no next-node 
            last = last.next  # jump to the next node 

        last.next = new_node # set the last node's next.node to the new_node 

    # Append a new node to the beginning of the linked list
    def prepend(self, data):
        new_node = SimpleNode(data)

        if not self.head:
            self.head = new_node
        
        new_node.next = self.head  # put new node at the beginning of the linked list

        self.head = new_node # set the new node as the head node 

    # delete given data value from linked list 
    def delete(self,data):
        """
        1. Iterate over linked list until you find the data --> current_node = data. 
        2. Delete the current_node by skipping over it 
        3. Update the next.node value for the node previous to the current node, to the current nodes next node
        """
        if not self.head:  # exit function if list is empty --> there is nothing to delete 
            return 
        
        if self.head.data == data:
            self.head = self.head.next 
            return 
        
        Prev_node = None
        Current = self.head 
        while Current and Current.data != data:  # iterate over linked list and, for each node, check if node.data = data to be deleted
            Prev_node = Current 
            Current = Current.next # jump to next node in each iteration 

        if Current == None:
            return # no match was found, data to be deleted is not in linked list
        
        # Current contains the data to be deleted. Now it (current) has to be skipped over in the linked list
        Prev_node.next = Current.next 
        
