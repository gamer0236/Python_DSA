from collections import deque

class Queue:
    def __init__(self):
        self.buffer  =deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
        

pq = Queue()
pq.enqueue(2)
pq.enqueue(3)
pq.enqueue(4)

print(pq.dequeue())

