class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key: int) -> int:
        return key % self.size

    def insert(self, key: int) -> None:
        index = self.hash_function(key)
        current = self.table[index]

        # Check if the key already exists
        while current:
            if current.key == key:
                return  # Key already exists, don't insert duplicate
            current = current.next

        # Insert at the end of the list
        new_node = Node(key)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key: int) -> bool:
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def delete(self, key: int) -> bool:
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next

        return False
