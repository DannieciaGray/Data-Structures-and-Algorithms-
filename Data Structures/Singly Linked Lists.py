# Singly Linked List Implementation

# linked list class 
class LinkedList:
    def __init__(self):
        self.head = None

    # Reverse the list and then display it.
    def reverse(self):
        prev = None  
        current = self.head

        while current != None:
            next_node = current.next # saves data
            current.next = prev     # reverse the current node's pointer
            prev = current          # move prev to the current node
            current = next_node     # move to the next node 
        
        #reassign head of list 
        self.head = prev


    # Delete a node by value and display the list after deletion.
    def delete_by_value(self,val):
        # start from head node
        temp = self.head

        # if head node holds the value
        if temp is not None and temp.data == val:
            # update head
            self.head = temp.next

            # Free old head
            temp = None
            return 
        
        # Initialized prev to None 
        prev = None

        # Traverse to find the value
        while temp is not None and temp.data != val:
            # keep track of the previous node
            prev = temp

            # move to the next node
            temp = temp.next

            # if key is not found,return
            if temp is None:
                return 
            
            # Unlink the node from the list
            prev.next = temp.next

            # Free the node 
            temp = None

    # Find and return the middle element of the list.
    def find_middle(self):
        current = self.head
        slow = current
        fast = current

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        return slow.data
    
    # Search for values in the list and print their positions.
    def find_vals(self,val):
        current = self.head
        position = 0
        found = False

        while current:
            # if value is found
            if current.data == val:
                print(f"Value {val} found at position {position}")
                found = True
            current = current.next
            position += 1
      
        # if value is not found 
        if not found:
            print(f"Value {val} not found in list")

# Insert values at different positions (beginning,end,and middle). Display list after each insertion
    def insert_beginning(self,data):
        # create a new node with given data
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return
        
        # set new node's next to the current head
        new_node.next = self.head

        # update head to the new node
        self.head = new_node

    def insert_middle(self,data):
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return
        slow =self.head
        fast = self.head
        prev = None  # To keep track of the node before 'slow'

        # Traverse the list to find the middle using the slow-fast pointer approach
        while fast and fast.next:
            prev = slow
            slow = slow.next 
            fast = fast.next.next

        # Insert the new node after 'prev' (before the middle node 'slow') 
        if prev:
            new_node.next = slow
            prev.next = new_node

        # If there's no 'prev', it means the list has only one element
        else:
            new_node.next = self.head
            self.head = new_node


    def insert_end(self, data):
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next

        # Link the new node at the end
        current.next = new_node

    
    def print_list(self):
        # Start from the head node
        current = self.head 

        # traverse the list 
        while current:
            # Print the data 
            print(current.data,end = " -->")

            # Move to the next node
            current = current.next
        
        print("None") # shows end of list


    # Display the list and its length.
    def get_length(self):
        current = self.head
        length = 0
        

        while current:
            current = current.next
            length += 1
      
        print(f"Length of list = {length}")

# node class
class Node:
    def __init__(self,data):
        # Store the data
        self.data = data

        # initialize next as None 
        self.next = None


# Testing Implementation

# Create a new LinkedList
llst = LinkedList()

# Insert elements at the beginning
llst.insert_beginning(10)
llst.insert_beginning(20)
llst.insert_beginning(30)

# Print the list
print("List after inserting at the beginning:")
llst.print_list()  # Output: 30 --> 20 --> 10 --> None

# Insert in the middle
llst.insert_middle(25)
print("List after inserting in the middle:")
llst.print_list()  # Output: 30 --> 25 --> 20 --> 10 --> None

# Insert at the end
llst.insert_end(5)
print("List after inserting at the end:")
llst.print_list()  # Output: 30 --> 25 --> 20 --> 10 --> 5 --> None

# Reverse the list
llst.reverse()
print("List after reversing:")
llst.print_list()  # Output: 5 --> 10 --> 20 --> 25 --> 30 --> None

# Find the middle element
middle = llst.find_middle()
print(f"Middle element: {middle}")  # Output: 20

# Search for values
llst.find_vals(25)  # Output: Value 25 found at position 3
llst.find_vals(50)  # Output: Value 50 not found in list

# Delete a node
llst.delete_by_value(20)
print("List after deleting a node:")
llst.print_list()  # Output: 5 --> 10 --> 25 --> 30 --> None

# Get the length of the list
llst.get_length()  # Output: Length of list = 4






