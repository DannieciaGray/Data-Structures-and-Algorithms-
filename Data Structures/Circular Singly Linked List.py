class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_first(self, data):
        new_node = Node(data)
        if not self.head:
            # If the list is empty, point new node to itself
            new_node.next = new_node
            self.head = new_node
        else:
            # Find the last node
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Insert at beginning
            new_node.next = self.head
            last.next = new_node  # Last node now points to the new head
            self.head = new_node  # Update head

    # Insert at the end
    def insert_last(self, data):
        new_node = Node(data)
        if not self.head:
            # If list is empty, make new node point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Insert at the end
            last.next = new_node
            new_node.next = self.head  # Maintain circular structure

    # Delete the first node
    def delete_first(self):
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            # If there's only one node
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next

            # Move head to next node and update last node's pointer
            self.head = self.head.next
            last.next = self.head

    # Delete the last node
    def delete_last(self):
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            # If only one node
            self.head = None
        else:
            prev = None
            current = self.head

            while current.next != self.head:
                prev = current
                current = current.next
            
            # Update second-to-last node's next pointer to head
            prev.next = self.head
