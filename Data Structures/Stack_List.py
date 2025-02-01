class StackList:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty, cannot pop"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty, cannot peek"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0

# Testing Stack using Python List
stack = StackList()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek()) # Output: 20
print(stack.pop())  # Output: 20
print(stack.pop())  # Output: 10
print(stack.pop())  # Output: Stack is empty, cannot pop
