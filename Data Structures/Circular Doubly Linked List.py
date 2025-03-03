class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None # Points to the previous node
        self.next = None # Points to the next node 


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None 

    
    # Function to add a node at the beginning
    def insert_first(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head 
            self.head.prev = self.head 

        else:
            tail = self.head.prev 
            new_node.next = self.head 
            new_node.prev = tail 
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    # Function to add a node at the end 
    def insert_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head 
            self.head.prev = self.head

        else:
            tail = self.head.prev 
            tail.next = new_node
            new_node.prev = tail 
            new_node.next = self.head 
            self.head.prev = new_node


    # Function to delete the first node in a list
    def delete_first(self):
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None 
            return 

        first = self.head 
        last = self.head.prev # get the last node 

        self.head = first.next # move head to the next node 
        self.head.prev = last  # update new head's prev to last node 
        last.next = self.head  # update last node's next to the new head 

        first.next = None 
        first.prev = None  
        

    # Function to delete the last node in a list 
    def delete_last(self):
        if not self.head:
            print("List is empty")
            return 
        
        current = self.head 

        while current.next != self.head:
            current = current.next 

        
        current.prev.next = self.head 
        self.head.prev = current.prev

        current.next = None 
        current.prev = None 