from aStar import *
from graph import *
from node import *
from UCS import *
from prioqueue import *
import os


filename = "./test/" + input("Masukkan nama file: ")
while not os.path.exists(filename):
    print("File tidak ditemukan. Silakan masukkan nama file yang benar\n")
    filename = "./test/" + input("Masukkan nama file: ")

print("\nMenampilkan graph...")
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


inputNode = int(input("Masukkan nomor node awal: "))
while inputNode < 1 or inputNode > graph.totalNode:
    inputNode = int(input("Node tidak ditemukan. Silakan masukkan node yang benar: "))
start = graph.nodeList[inputNode-1].name

inputNode = int(input("Masukkan nomor node tujuan: "))
while inputNode < 1 or inputNode > graph.totalNode:
    inputNode = int(input("Node tidak ditemukan. Silakan masukkan node yang benar: "))
goal = graph.nodeList[inputNode-1].name

print("\n1. A* Search \n2. UCS Search")
choice = input("Masukkan pilihan: ")
while choice != "1" and choice != "2":
    choice = input("Silakan masukkan pilihan yang benar: ")

if choice == "1":
    result = aStar(start, goal, graph)
elif choice == "2":
    result = UCS(start, goal, graph)
print("\nHasil: " + result.name)
print("Jarak: " + str(round(result.gn,2)) + " km\n")
visualize = input("Tampilkan visualisasi? (y/n): ")
if visualize == "y" or visualize == "Y":
    name = " "
    while " " in name:
        name = input("Masukkan nama arsip peta yang ingin disimpan (tanpa format dan spasi): ")
    displayGraph(graph, result)
    displayMap(graph, start, goal, result, name)


