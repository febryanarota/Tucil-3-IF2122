import networkx as nx
import matplotlib.pyplot as plt
from graph import *
from node import *

def isNodeValid(nodeName, graph):
    for n in graph.nodeList:
        if nodeName == n.name:
            return True
    return False

def findNodeByName(nodeName, graph):
    for n in graph.nodeList:
        if nodeName == n.name:
            return n
        
def aStar(startName, goalName, graph):
    #A* search algorithm
    start = findNodeByName(startName, graph)
    start.path = [start]
    goal = findNodeByName(goalName, graph)

    queue = []
    queue.append(start)

    while len(queue) > 0:
        # Pop the first element
        current = queue.pop(0)

        # Check if current node is goal
        if current == goal:
            return current
        
        listNewNode = []
        for neighbor in current.neighbors:
            # Create new node with new path
            hn = neighbor.calculateHaversine(goal)
            gn = current.gn +   current.calculateHaversine(neighbor)
            fn = current.fn + hn + gn

            newNode = Node(current.name + " -> " + neighbor.name, neighbor.x, neighbor.y)
            newNode.path = current.path + [neighbor]
            newNode.neighbors = neighbor.removeNeighbor(newNode.path)
            newNode.setValue(gn, hn, fn)
            
            listNewNode.append(newNode)

            if hn == 0:
                return newNode
            else:
                queue.append(newNode)
        
        # Sort the list and add to queue
        listNewNode.sort(key=lambda x: x.fn)
        queue = listNewNode + queue

def displayGraph(graph, result = Node()):
    # Display graph
    g = nx.Graph()
    for node in graph.nodeList:
        g.add_node(node.name)

        for neighbor in node.neighbors:
            if neighbor in result.path and node in result.path:
                g.add_edge(node.name, neighbor.name, color='r', weight= round(node.calculateHaversine(neighbor), 2))
            else:
                g.add_edge(node.name, neighbor.name, color='black', weight= round(node.calculateHaversine(neighbor), 2))

    pos = nx.spring_layout(g)
    edges,colors = zip(*nx.get_edge_attributes(g, 'color').items())
    nx.draw(g, pos, edgelist=edges, edge_color=colors, with_labels = True, font_weight = 'bold')
    edge_weight = nx.get_edge_attributes(g, 'weight') 
    nx.draw_networkx_edge_labels(g, pos, edge_labels = edge_weight)
    plt.show()



                
            
        