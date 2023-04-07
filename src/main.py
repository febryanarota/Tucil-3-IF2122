from aStar import *
from graph import *
from node import *
import os


filename = "./test/" + input("Masukkan nama file: ")
while not os.path.exists(filename):
    print("File tidak ditemukan. Silakan masukkan nama file yang benar")
    filename = "./test/" + input("Masukkan nama file: ")

print("\n Menampilkan graph...")
print("*Close graph untuk melanjutkan...")
graph = Graph(filename)
graph.readGraph()
displayGraph(graph) # display graph without path

print("===================")
print("Daftar node: ")
i = 1
for node in graph.nodeList:
    print(f"{i}. {node.name}")
    i+=1
print("===================")


start = input("Masukkan node awal: ")
while not isNodeValid(start, graph):
    start = input("Node tidak ditemukan. Silakan masukkan node yang benar: ")

goal = input("Masukkan node tujuan: ")
while not isNodeValid(goal, graph):
    goal = input("Node tidak ditemukan. Silakan masukkan node yang benar: ")

print("\n1. A* Search \n2. UCS Search")
choice = input("Masukkan pilihan: ")
while choice != "1" and choice != "2":
    choice = input("Silakan masukkan pilihan yang benar: ")

if choice == "1":
    result = aStar(start, goal, graph)
    print("\nHasil: " + result.name)
    visualize = input("Tampilkan visualisasi? (y/n): ")
    if visualize == "y" or visualize == "Y":
        displayGraph(graph, result)



