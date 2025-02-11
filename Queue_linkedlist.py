#Implenting queue operations using singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Queue:
    def __init__(self):
        self.front = None # Points to the front node (head of linked list)
        self.rear  = None # Points tp the rear node (tail of the linked list)
        self._size = 0

    # Dequeue operation (remove and return the front element of the queue)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        temp = self.front 
        self.front = self.front.next # Move front to the next node
        if self.front is None: #if the queue becomes empty 
            self.rear = None
        self._size -= 1
        print(f"Dequeued: {temp.data}")
        return temp.data

    # Enqueue operation 
    def enqueue(self,item):
        new_node = Node(item)
        if self.rear is None: # if queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued: {item}")

    #checks if queue is empty 
    def is_empty(self):
        return self.front is None 
    
    # Return the size of the queue
    def size(self):
        return self._size

    # Peek at the front element without removing it
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data
    
#Test cases
q = Queue()

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
