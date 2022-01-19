# Maze solving 
Robots nowadays is a major component due to its ability to plan its path. You can program a robot for all possible motions in order to accomplish specific task. However, preprogramming a robot for all possible cases might meet is an impossible thing, due to the fact that number of motions can be an infinite loop or large number of motions. 
We will show you in this project the application of the Artificial Intelligent (search algorithm especially), robot path planning (e.g. A*) and how will it find its optimal path like humans and how they are able to see their obstacles and finding their optimal path in real life.

## Getting Started
**Requirements**

Install the necessary requirmenets by running:

``` bash
    pip install -r requirements.txt
```

**Running**

1. Open a terminal and cd to the project directory and run readfile.py:
``` bash
   python3 readfile.py
```
2. Enter initial state X and Y
  ``` bash
 Welcome :)
Enter Initial state
X=
Y=
```
3. Enter your Goal state 
``` bash
   Enter your goal
X=
Y=
```
4. Choose an algorthim.
``` bash
1- BFS
2- DFS
3- Greedy
4- A*
Enter number of algrithm: 
```



## Desing Classes
Classes Description
> **Breadth First Search (BFS)**

 -A class initiated by initial state to find the goal state in BFS search algorithm.

> **Depth First Search (DFS)**

 -A class initiated by initial state to find the goal state in DFS search algorithm

> **Astar**

 -A class initiated by initial state to find the goal state by calculate F(n) and find the less costly path “Optimal path”.
 
> **Greedy**

 -A class initiated by initial state to find the goal state by Finding the less costly path “G(n)”.

> **Node**

 -A node class that helps search algorithms (BFS and DFS) to move and navigate its coordinate.

> **main**

 -Used to read an image in a specific location in computer and convert it into 2D-array and it has a main which triggers the whole program.

> **NodeH**

 -A node class that helps the specific heuristic search algorithms Greedy. to  move and navigate its coordinate.

> **NodeHA**

 -A node class that helps the specific heuristic search algorithms A*. to move and navigate its coordinate.




## Implementation 
- In Class Node “BFS and DFS’s Node”
    - __init__(self,x,y,nim): A default constructor to store coordinate and data as attributes.
    - MoveToRight(self): Moving the node to right and append it to childering.
    - MoveToLift(self): Moving the node to left and append it to childering.
    - MovetoUp(self): Moving the node upward and append it to childering.
    - MoveToDown(self): Moving the node Downward and append it to childering.
    - isGoal(self,x,y): To check whether the coordinate (x,y) is reached the goal state or not.
    -  print(self): Prints the coordinate (x,y).
    -  ExpandMove(self): To Expand the move for the four directions (up,down,left,right)

- In Class BFS
  - Search(self, root, goalx, goaly): it starts the BFS search algorithm which uses queue and checks if it is the solution or not ,if it is not it inters into the children and checks if one of them is the solution or not, if not it will add to the queue .The Search method begins the BFS by taking the root and the coordinate(x,y) to find the goal state. We implemented a while to help finding the goal. Then we implemented a for loop in it to search for children and look if they the goal or not if not add children to the white list and black list
  - findpath(self, go, lis=[]): The goal is to find the path from the given go and append it to a given lis[] until there are not any parent

- In Class DFS
  - Search(self, root, goalx, goaly): Begins the DFS search algorithm by taking the root and the coordinate(x,y) to find the goal state. We implemented a while to help finding the goal in the following condition. Then we implemented a for loop in it to search for children and look if they the goal or not if not add children to the white list and black list

  - findpath(self, go, lis=[]): The goal is to find the path from the given go and append it to a given lis[] until there are not any parent.
- In Class Greedy
  - Search(self, root, goalx, goaly): Begins the Greedy search algorithm by taking the root and the coordinate(x,y) to find the goal state. We implemented a while to help finding the goal in the following condition. Then we implemented a for loop in it to search for children and look if they the goal or not if not add children to the white list and black list.
  - findpath(self, go, lis=[]): The goal is to find the path from the given go and append it to 
a given lis[] until there are not any parent

- In Class NodeH “Greedy’s Node”
  - __init__(self,x,y,nim,goalX,goalY,cost,chose): A default constructor to store coordinate and data as attributes. It contains a Manhattan and Euclidean choice. If the choice is 1 so the HU will be in Manhattan way else it will be Euclidean.
  -  _it_(self,other): it returns true if fcost< the given fcost.
  - MoveToRight(self): Moving the node to right and append it to childering.
  - MoveToLift(self): Moving the node to left and append it to childering.
  - MovetoUp(self): Moving the node upward and append it to childering.
  - MoveToDown(self): Moving the node Downward and append it to childering.
  - isGoal(self,x,y): To check whether the coordinate (x,y) is reached the goal state or not.
  - print(self): Prints the coordinate (x,y).
  - ExpandMove(self): To Expand the move for the four directions (up,down,left,right).
  - Manhattan(self): It finds the heuristic in Manhattan way and returns heuristic x + heuristic y.
  - Euclidean(self): It finds the heuristic in Euclidean way, heuristicX*heuristicX and heuristicY*heuristicY then compine the result after that returns the square root of result on result.

- In Class NodeHA “A*’s Node”
  - __init__(self,x,y,nim,goalX,goalY,cost,chose): A default constructor to store coordinate and data as attributes. It contains a Manhattan and Euclidean choice. If the choice is 1 so the HU will be in Manhattan way else it will be Euclidean.
  - _it_(self,other): it returns true if fcost< the given fcost.
  - MoveToRight(self): Moving the node to right and append it to childering.
  - MoveToLift(self): Moving the node to left and append it to childering.
  - MovetoUp(self): Moving the node upward and append it to childering.
  - MoveToDown(self): Moving the node Downward and append it to childering.
  - isGoal(self,x,y): To check whether the coordinate (x,y) is reached the goal state or not.
  - print(self): Prints the coordinate (x,y).
  - ExpandMove(self): To Expand the move for the four directions (up,down,left,right).
  - Manhattan(self): It finds the heuristic in Manhattan way and returns heuristic x + heuristic y.
  - Euclidean(self): It finds the heuristic in Euclidean way,heuristicX*heuristicX and heuristicY*heuristicY then compine the result after that returns the square root of result on result.
- In Class NodeHA “A*’s Node”
  - __init__(self,x,y,nim,goalX,goalY,cost,chose): A default constructor to store coordinate and data as attributes. It contains a Manhattan and Euclidean choice. If the choice is 1 so the HU will be in Manhattan way else it will be Euclidean.
  - _it_(self,other): it returns true if fcost< the given fcost.
  - MoveToRight(self): Moving the node to right and append it to childering.
  - MoveToLift(self): Moving the node to left and append it to childering.
  - MovetoUp(self): Moving the node upward and append it to childering.
  - MoveToDown(self): Moving the node Downward and append it to childering.
  - isGoal(self,x,y): To check whether the coordinate (x,y) is reached the goal state or not.
  - print(self): Prints the coordinate (x,y).
  - ExpandMove(self): To Expand the move for the four directions (up,down,left,right).
  - Manhattan(self): It finds the heuristic in Manhattan way and returns heuristic x+ heuristic y. 
  - Euclidean(self): It finds the heuristic in Euclidean way, heuristicX*heuristicX and heuristicY*heuristicY then compine the result after that returns the square root of result on result.
  
- In Class Astar
  - Search(self, root, goalx, goaly): Begins the A* search algorithm by taking the root and the coordinate(x,y) to find the goal state, We implemented a while to help finding the goal in the following condition. Then we implemented a for loop in it to search for children and look if they the goal or not if not add children to the white list and black list. 
  - findpath(self, go, lis=[]): The goal is to find the path from the given go and append it to a given lis[] until there are not any parent.

- In the main class: 
  - Is where we read an image and insert it into 2D-array and it contain the main methods which start any search algorithm.


## Result
![alt text](https://github.com/mralwaleed/maze-solving/blob/gh-pages/Result/A_Star_Manhattan.png)

