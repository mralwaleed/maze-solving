from PIL import Image
import numpy as np

# Open the maze image and make greyscale, and get its dimensions
from PIL._imaging import display
from Astar import Astar
from BSF import BFS
from DFS import DFS
from Greedy import Greedy
from Node import Node
from NodeH import NodeH
from NodeHA import NodeHA



image = Image.open('maze.jpg').convert('L')
outimg = image.load()
binary = image.point(lambda p: p > 128 and 1)
data = np.array(binary)
root = None
print("Welcome :) ")
print("Enter Initial stat ")
x, y = int(input("X=")), int(input("Y="))
print("Enter your goal ")
gx, gy = int(input("X=")), int(input("Y="))

print("1- BFS \n"
       "2- DFS \n"
         "3- Greedy \n"
           "4- A* ")

chois = -1
while (chois == -1):
   chois = int(input("Enter number of algrithm "))
   if (chois == 1):
        root = Node(x, y,data)
        list = BFS().Search(root, gx, gy)
   elif (chois == 2):
        root = Node(x, y,data)
        list = DFS().Search(root, gx, gy)
   elif (chois == 3):
        print("Enter the calculation method \n1-Manhattan\n2-Euclidean")
        c = int(input())
        root = NodeH(x, y,data, gx, gy, c)
        list = Greedy().Search(root, gx, gy)
   elif (chois == 4):
        print("Enter the calculation method \n1-Manhattan\n2-Euclidean")
        c = int(input())
        root = NodeHA(x, y,data, gx, gy, 0, c)
        list = Astar().Search(root, gx, gy)
   else:
            chois = -1
            print("Enter wrong :)")

   for a in range(len(list)):
      outimg[list[a].y, list[a].x] = 150

   image.show()
