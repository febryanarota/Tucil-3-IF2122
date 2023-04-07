import math

class Node:
    def __init__(self, name, x, y):
        # Constructor Node
        self.name = name
        self.x = x
        self.y = y
        self.gn = 0
        self.hn = 0
        self.fn = 0
        self.path = []
        self.neighbors = []

    def __lt__ (self, other):
        return self.fn < other.fn

    def getDistance(self, other):
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
    
    def updateNeighbors(self, neighbors, removeNeighbor):
        # Update the neighbors of the node
        self.neighbors = neighbors
        self.neighbors.remove(removeNeighbor)

    def setValue(self, gn, hn, fn):
        # Update the value of the node
        self.gn = gn
        self.hn = hn
        self.fn = fn

    def updatePath(self, path):
        # Update the path of the node
        self.path = path

    def displayNodeInfo(self):
        # Display the node information

        print("--------------------")
        print("Node:", self.name)
        print("ID:", self.id)
        print("X,Y:",self.x,",",self.y)

        for node in self.neighbors:
            print()
            print("Neighbor:", node.name)
            print("Distance:", self.getDistance(node))

    # def addNeighbor(self, neighbor, distance):
    #     self.neighbors[neighbor] = distance


    

        
        


        