import math


class Node:
    """Represents a single cell in the maze grid.

    Supports optional heuristic computation (Manhattan or Euclidean) and
    cumulative cost tracking for informed search algorithms like Greedy and A*.
    """

    def __init__(self, x, y, grid, goal_x=None, goal_y=None, cost=0, heuristic=None):
        self.x = x
        self.y = y
        self.parent = None
        self.children = []
        self.grid = grid
        self.location = f"({x},{y})"

        self.goal_x = goal_x
        self.goal_y = goal_y
        self.cost = cost
        self.heuristic_type = heuristic

        if heuristic == "manhattan":
            self.h = self._manhattan()
        elif heuristic == "euclidean":
            self.h = self._euclidean()
        else:
            self.h = 0

        self.f = self.h + self.cost

    def __lt__(self, other):
        return self.f < other.f

    # --- Movement ---

    def move_right(self):
        if self.y + 1 < len(self.grid[self.x]) and self.grid[self.x][self.y + 1] == 1:
            child = Node(self.x, self.y + 1, self.grid,
                         self.goal_x, self.goal_y, self.cost + 1, self.heuristic_type)
            child.parent = self
            self.children.append(child)

    def move_left(self):
        if self.y - 1 >= 0 and self.grid[self.x][self.y - 1] == 1:
            child = Node(self.x, self.y - 1, self.grid,
                         self.goal_x, self.goal_y, self.cost + 1, self.heuristic_type)
            child.parent = self
            self.children.append(child)

    def move_up(self):
        if self.x - 1 >= 0 and self.grid[self.x - 1][self.y] == 1:
            child = Node(self.x - 1, self.y, self.grid,
                         self.goal_x, self.goal_y, self.cost + 1, self.heuristic_type)
            child.parent = self
            self.children.append(child)

    def move_down(self):
        if self.x + 1 < len(self.grid) and self.grid[self.x + 1][self.y] == 1:
            child = Node(self.x + 1, self.y, self.grid,
                         self.goal_x, self.goal_y, self.cost + 1, self.heuristic_type)
            child.parent = self
            self.children.append(child)

    def expand(self):
        self.move_left()
        self.move_right()
        self.move_down()
        self.move_up()

    def is_goal(self, goal_x, goal_y):
        return self.x == goal_x and self.y == goal_y

    # --- Heuristics ---

    def _manhattan(self):
        return abs(self.goal_x - self.x) + abs(self.goal_y - self.y)

    def _euclidean(self):
        return int(math.sqrt((self.goal_x - self.x) ** 2 + (self.goal_y - self.y) ** 2))

    @staticmethod
    def trace_path(node):
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = current.parent
        return path
