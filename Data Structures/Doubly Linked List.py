# Node class 
class ListNode:
    def __init__(self, data: any) -> None:
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

# Doubly linked list 
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node

    # Insert at the beginning
    def insert_first(self, value: int) -> None:
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update head to new node

    # Insert at the end
    def insert_last(self, value: int) -> None:
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  # Update tail to new node

    # Delete a node
    def delete_node(self, value: int) -> None:
        current = self.head
        if current is None:
            return

        if current.data == value:  # If head is to be deleted
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # Update tail if list is empty
            del current
            return

        while current and current.data != value:
            current = current.next

        if current is None:
            return

        if current.next:  # If not the last node
            current.next.prev = current.prev
        else:
            self.tail = current.prev  # Update tail if deleting last node

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

    # Insert after a given node value
    def insert_after(self, node: int, value: int) -> None:
        new_node = ListNode(value)
        current = self.head

        while current:
            if current.data == node:
                new_node.next = current.next
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node  # Update tail if new last node
                current.next = new_node
                return
            current = current.next

    # Get length of the list
    def length(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Reverse the linked list
    def reverse(self) -> None:
        current = self.head
        self.tail = self.head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        self.head = prev  # Update head pointer

    # Remove duplicates from a **sorted** doubly linked list
    def remove_duplicates(self) -> None:
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                duplicate = current.next
                current.next = duplicate.next
                if duplicate.next:
                    duplicate.next.prev = current
                else:
                    self.tail = current  # Update tail if last node removed
            else:
                current = current.next

    # Rotate list by n positions
    def rotate(self, n: int) -> None:
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
        self.tail = current  # Update tail to new last node

        last = new_head
        while last.next:
            last = last.next

        last.next = self.head
        self.head.prev = last
        self.head = new_head  # Update head pointer
