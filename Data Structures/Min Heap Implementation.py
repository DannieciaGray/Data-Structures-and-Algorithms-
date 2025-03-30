class PriorityQueue:
    def __init__(self):
        # Initialize an empty priority queue using a list 
        self.queue = []

    def insert(self,item):
        # Inserts a new item into the priority queue
        self.queue.append(item)
        self.queue.sort()  # Keep it sorted after each insert

    def peek(self):
        # Returns the minimum element without removing it
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]

    def extract(self):
        # Removes and returns the minimum element 
        if self.is_empty():
            print("Queue is empty")
            return None
        min_val = self.queue[0]
        self.queue.pop(0)
        return min_val
    

    def is_empty(self):
        # Returns True if the queue is empty, otherwise False
        return len(self.queue) == 0

    def length(self):
        # Returns the number of elements in the priority queue 
        return len(self.queue)


