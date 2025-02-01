class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            return "stack is empty, cannot pop"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            return "stack is empty, cannot peek"
        return self.top.data
    
    def is_empty(self):
        return self.top is None

# Testing stack using Singly Linked List
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek()) # Output: 20
print(stack.pop())  # Output: 20
print(stack.pop())  # Output: 10
print(stack.pop())  # Output: stack is empty, cannot pop


