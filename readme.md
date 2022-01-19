# Maze solving 
Robots nowadays is a major component due to its ability to plan its path. You can program a robot for all possible motions in order to accomplish specific task. However, preprogramming a robot for all possible cases might meet is an impossible thing, due to the fact that number of motions can be an infinite loop or large number of motions. 
We will show you in this project the application of the Artificial Intelligent (search algorithm especially), robot path planning (e.g. A*) and how will it find its optimal path like humans and how they are able to see their obstacles and finding their optimal path in real life.

## Getting Started
**Requirements**

Install the necessary requirmenets by running:

``` bash
    pip install -r requirements.txt
```

**Running **

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



