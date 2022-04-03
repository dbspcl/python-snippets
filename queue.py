# Queue implementation in Python
# Uses an array to represent the queue
# Python has append and pop functions that can be used against the array - use pop(0) to pop the first entry on the queue
# Check for empty is to see if length of array is 0

class Queue:
    def __init__(self):
        self.queue = []
    # Add an element
    def enqueue(self, item):
        self.queue.append(item)
    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    # Display  the queue
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
