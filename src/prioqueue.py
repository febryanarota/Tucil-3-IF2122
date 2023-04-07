from graph import *
from node import *

class PrioQueue:
    # def __init__(self):
    #     self.route = []
    #     self.
    def __init__(self):
        self.queue = []

    def enqueue(self, node):
        if (self.is_empty(self)):
            self.queue.append(node)
        else:
            for i in range(len(self.queue)):
                if (self.queue[i].gn > node.gn):
                    self.queue.insert(i, node)
                    break

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0