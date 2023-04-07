from node import *

class Graph:
    def __init__(self, file):
        # Constructor Graph
        self.file = file
        self.nodeList = []
        self.totalNode = 0

    def readGraph(self):
        # Read the graph from the file
        read = open(self.file, "r")

        # Read the total number of nodes
        self.totalNode = int(read.readline())

        # Read the nodes and append them to the nodeList
        id = 1
        for i in range(self.totalNode):
            line = read.readline().split()
            self.nodeList.append(Node(line[0], float(line[1]), float(line[2])))
            id += 1
        
        # Read the adjacency matrix
        for i in range(self.totalNode):
            line = read.readline().split()
            for j in range(self.totalNode):
                if(line[j] == "1"):
                    self.nodeList[i].neighbors.append(self.nodeList[j])
    
# test = Graph("./testtest.txt")
# test.readGraph()
# for node in test.nodeList:
#     node.displayNodeInfo()