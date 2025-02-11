#Implenting queue operations using python lists
class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None 
        dequeued_item = self.queue.pop(0)  # Remove the first element 
        
        return dequeued_item


    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]
    

# Test cases
q = QueueList()

# Test enqueue operation
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Test dequeue operation
q.dequeue()
q.dequeue()

# Test peek operation
print(f"Front element: {q.peek()}")  # Expected: 30

# Test is_empty method
print(f"Is queue empty? {q.is_empty()}")  # Expected: False

# Test dequeue until empty
q.dequeue()
print(f"Is queue empty? {q.is_empty()}")  # Expected: True

# Test dequeue on an empty queue (underflow)
q.dequeue()  # Expected: "Queue is empty, cannot dequeue"


