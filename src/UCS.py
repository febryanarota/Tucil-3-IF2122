from node import *
from graph import *
from prioqueue import *

def UCS(startName, goalName, graph):
    # Finding startNode in the graph. Initializing starting path aswel.
    startNode = graph.findNodeByName(startName)
    startNode.path = [startNode]

    # Finding goalNode in the graph.
    goalNode = graph.findNodeByName(goalName)
    route = PrioQueue()
    # Enqueue the first node at the first tested node
    route.enqueue(startNode)

    # Loop until goal node reached
    while not route.is_empty():
        # Dequeue first node with smallest current gn
        current = route.dequeue()
        # Check if current node is goal or current path has reached goal
        if current == goalNode or goalNode in current.path:
            # Goal has been found with gn value, current Node has reached goal and the search ends
            return current
        for neighbor in current.neighbors:
            # Create new node and update path based on current node neighbors
            gn = current.gn + current.calculateHaversine(neighbor)
            # Node is now a series of nodes
            newNode = Node(current.name + " -> " + neighbor.name, neighbor.x, neighbor.y)
            newNode.path = current.path + [neighbor]
            # Initialize the new node neighbors as its current self
            newNode.neighbors = neighbor.neighbors
            # Removing visited node from new node neighbors
            newNode.neighbors = neighbor.removeNeighbor(newNode.path)
            newNode.gn = gn

            # Adding node to the queue
            route.enqueue(newNode)


