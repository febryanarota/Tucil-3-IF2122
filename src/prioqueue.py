from graph import *
from node import *

class PrioQueue:
    def __init__(self):
        # Constructor PrioQueue
        self.queue = []

    def enqueue(self, node):
        # Enqueue based on gn value (ascending inside queue).
        biggest = True
        if (self.is_empty()):
            self.queue.append(node)
        else:
            for i in range(len(self.queue)):
                # Finding bigger gn than node to be enqueued
                if (self.queue[i].gn > node.gn):
                    self.queue.insert(i, node)
                    biggest = False
                    break
            # Insert last if node turns out to be the biggest
            if biggest:
                self.queue.append(node)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0