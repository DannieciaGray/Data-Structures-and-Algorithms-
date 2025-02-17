# Node class 
class ListNode:
    def __init__(self, data: any):
        self.data = data
        self.prev = None  # Points to the previous node
        self.next = None  # Points to the next node

# Doubly linked list 
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    # Insert at the beginning
    def insert_first(self, value: int):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update head to new node

    # Insert at the end
    def insert_last(self, value: int):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node

        last.next = new_node
        new_node.prev = last  # Maintain doubly linked structure

    # Delete a node
    def delete_node(self, value: int):
        current = self.head
        if current is None:
            print("List is empty!")
            return

        if current.data == value:  # If head is to be deleted
            self.head = current.next
            if self.head:
                self.head.prev = None
            del current  # Properly delete the node
            return

        while current and current.data != value:
            current = current.next

        if current is None:
            print(f"Node with the value {value} not found!")
            return

        if current.next:  # If not the last node
            current.next.prev = current.prev

        if current.prev:  # If not the first node
            current.prev.next = current.next

        del current  # Properly delete the node

    # Search for a node
    def search_node(self, value: int) -> bool:
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Insert after a given node
    def insert_after(self, node: int, value: int):
        new_node = ListNode(value)
        current = self.head

        while current:
            if current.data == node:
                new_node.next = current.next
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

        print(f"{node} is not in the list. Therefore, {value} cannot be inserted.")

    # Get the length of the list
    def length(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Reverse the list
    def reverse(self):
        current = self.head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        self.head = prev  # Update head pointer

    # Remove duplicates
    def remove_duplicates(self):
        current = self.head
        seen = set()  # Track seen values
        while current:
            if current.data in seen:
                prev_node = current.prev
                prev_node.next = current.next
                if current.next:
                    current.next.prev = prev_node
            else:
                seen.add(current.data)
            current = current.next

    # Rotate the list by n positions
    def rotate(self, n: int):
        if not self.head or n == 0:
            return  # No rotation needed

        length = self.length()
        n = n % length  # Normalize n

        if n == 0:
            return  # No rotation needed

        current = self.head
        for _ in range(length - n - 1):
            current = current.next

        new_head = current.next
        new_head.prev = None
        current.next = None

        last = new_head
        while last.next:
            last = last.next

        last.next = self.head
        self.head.prev = last

        self.head = new_head  # Update head pointer
