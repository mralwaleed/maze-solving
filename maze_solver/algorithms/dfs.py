from collections import deque

from maze_solver.node import Node


class DFS:
    """Depth-First Search — fast but does not guarantee the shortest path."""

    def search(self, root, goal_x, goal_y):
        open_list = deque([root])
        visited = {root.location: True}

        while open_list:
            current = open_list.pop()
            current.expand()

            if current.is_goal(goal_x, goal_y):
                return Node.trace_path(current)

            for child in current.children:
                if child.is_goal(goal_x, goal_y):
                    return Node.trace_path(child)
                if child.location not in visited:
                    open_list.append(child)
                    visited[child.location] = True

        return []
