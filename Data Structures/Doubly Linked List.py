# node class 
class ListNode:
    def __init__(self,data:any):
        self.data = data
        self.prev = None # points to the previous node
        self.next = None # points to the next node 

# doubly linked list 
class DoublyLinkedList:
    def __init__(self):
        self.head = None # Initialize head to None 

    # insert_first method (inserts at the beginning)
    def insert_first(self,value:int):
        new_node = value 
        if self.head is None:
            self.head = new_node
        
        else:
            new_node = self.head 
            self.head.prev = new_node
            self.head = new_node

    # insert_last method
    def insert_last(self,value: int):
        new_node = value
        last = self.head
        if self.head is None:
            self.head.next = new_node
            return 

        else: 
            while last.next:
                last = last.next 
            last.next = new_node
            new_node.prev = last 

    # delete_node method
    def delete_node (self,value: int):
        current = self.head 
        if current is None:
            print("List is empty!")
            return 
        
        if current.data == value: # if head node itself holds the value 
            self.head = current.next
            if self.head : # if there is a next node, set its prev to None 
                self.head.prev = None 
            current = None 
            return 
        
        while current and current.data != value:
            current = current.next 

        if current is None:
            print(f"Node with the value {value} not found!")
            return 
        if current.next: # Node to be deleted is not the last node 
            current.next.prev = current.prev 
        
        if current.prev: # Node to be deleted is not the first node 
            current.prev.next = current.next 

        current = None 


    # search_node method
    def search_node(self,node: int, value: int):
        current = self.head 
        if current is None:
            print("List is empty!")
            return False 
        
        while current:
            if current.data == value:
                return True 
            current = current.next
        return False 

        

    # insert_after method 
    def insert_after(self,node: int, value: int):
        new_node = ListNode(value) 
        current = self.head 

        if current is None:
            print("List is empty!")
            return

        while current: 
            if current.data == node: # Find the target node
                new_node.next = current.next 
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node # Adjust next node's prev pointer
                current.next = new_node # Insert new node after current
                return  # Successfully inserted, exit function 
            current = current.next # Move to the next node 

        return(f"{node} is not in the list. Therefore, {value} cannot be inserted.")
      

    # length method 
    def length(self):
        length = 0 
        current = self.head 
        while current:
            current = current.next # iterate through list until value is None
            length += 1 # increase length by 1
        
        return length



    # reverse method
    def reverse(self):
        prev = None 
        current = self.head 

        while current:
            next_node = current.next 
            current.next = prev
            prev = current 
            current = next_node
            
        self.head = prev
            

    # remove duplicates method
    def remove_duplicates(self):
        pass

    # rotate method 
    def rotate(self,n: int):
        pass 

    

