import networkx as nx
import matplotlib.pyplot as plt
import plotly.express as px
import webbrowser
import folium
from graph import *
from node import *

def isNodeValid(nodeName, graph):
    # Check if node is on the graph
    for n in graph.nodeList:
        if nodeName == n.name:
            return True
    return False

def findNodeByName(nodeName, graph):
    # Return node by name
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

            # Update the attributes of the new node
            newNode = Node(current.name + " -> " + neighbor.name, neighbor.x, neighbor.y)
            newNode.path = current.path + [neighbor]
            newNode.setValue(gn, hn, fn)

            # Remove the visited node from the new node neighbors
            newNode.neighbors = neighbor.removeNeighbor(newNode.path)

            # Append the new node to the list for sorting
            listNewNode.append(newNode)

            # Check if the goal node is found
            if hn == 0:
                return newNode
        
        # Sort the new node list and add to queue
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

def displayMap(graph, start, goal, result):
    # Display map
    startNode = graph.findNodeByName(start)
    goalNode = graph.findNodeByName(goal)

    m = folium.Map(location=[startNode.x, startNode.y], zoom_start=50)
    for node in graph.nodeList:
        if node.name == start:
            folium.Marker([node.x, node.y], popup=node.name, icon=folium.Icon(color="red")).add_to(m)
        elif node.name == goal:
            folium.Marker([node.x, node.y], popup=node.name, icon=folium.Icon(color="green")).add_to(m)
        else:
            folium.Marker([node.x, node.y], popup=node.name).add_to(m)
        for neighbor in node.neighbors:
            distance = node.calculateHaversine(neighbor)
            if neighbor in result.path and node in result.path:
                folium.PolyLine(locations=[[node.x, node.y], [neighbor.x, neighbor.y]], color="red", weight=2.5, opacity=1, popup= str(distance)).add_to(m)
            else:
                folium.PolyLine(locations=[[node.x, node.y], [neighbor.x, neighbor.y]], color="blue", weight=2.5, opacity=1, popup= str(distance)).add_to(m)
        
    m.save('map.html')
    webbrowser.open_new_tab('map.html')

                
            
        