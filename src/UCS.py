from node import *
from graph import *
from prioqueue import *

def UCS(startName, goalName, graph):
    startNode = graph.findNodeByName(startName)
    goalNode = graph.findNodeByName(goalName)

    route = PrioQueue()
    route.queue.enqueue(startNode)
    while not route.is_empty():
        # Dequeue first node with smallest gn
        current = route.queue.dequeue()

        # Check if current node is goal or current path has reached goal
        if current == goalNode or goalNode in current.path:
            return current
        for neighbor in current.neighbors:
            # Create new node and update path based on current node neighbors
            gn = current.gn + current.calculateHaversine(neighbor)

            newNode = Node(current.name + " -> " + neighbor.name, neighbor.x, neighbor.y)
            newNode.path = current.path + [neighbor]
            newNode.neighbors = neighbor.removeNeighbor(newNode.path)
            newNode.gn = gn

            route.queue.enqueue(newNode)

