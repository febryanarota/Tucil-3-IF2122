from math import *

class Node:
    def __init__(self, name = "", x = 0, y = 0):
        # Constructor Node
        self.name = name
        self.x = x
        self.y = y
        self.gn = 0
        self.hn = 0
        self.fn = 0
        self.path = []
        self.neighbors = []

    def getDistance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def calculateHaversine(self, otherNode):
    # Earth Radius, Get Haversine in KM
        earthRadius = 6371
        
        # Convert Longitude and Latitude to Radians
        lat1 = radians(self.x)
        long1 = radians(self.y)
        lat2 = radians(otherNode.x)
        long2 = radians(otherNode.y)
        # Get the difference
        latDiff = lat2 - lat1
        longDiff = long2 - long1
        # Haversine
        a = (sin(latDiff / 2)**2) + (cos(lat1) * cos(lat2) * sin(longDiff / 2)**2)
        c = 2 * asin(sqrt(a))   
        return(c* earthRadius)

    def setValue(self, gn, hn, fn):
        # Update the value of the node
        self.gn = gn
        self.hn = hn
        self.fn = fn

    def displayNodeInfo(self):
        # Display the node information
        print("Node:", self.name)
        print("X,Y:",self.x,",",self.y)
        print(f"hn, gn, fn:  {round(self.hn, 2)}; {round(self.gn, 2)}; {round(self.fn, 2)}")
        for node in self.neighbors:
            print()
            print("Neighbor:", node.name)
            print("Distance:", self.getDistance(node))

    def removeNeighbor(self, path):
        for node in self.neighbors:
            if node in path:
                self.neighbors.remove(node)
        return self.neighbors