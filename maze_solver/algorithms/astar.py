import heapq

from maze_solver.node import Node


class AStar:
    """A* Search — combines actual cost and heuristic to find the optimal path."""

    def search(self, root, goal_x, goal_y):
        open_list = []
        heapq.heappush(open_list, (root.f, root))
        visited = {root.location: True}

        while open_list:
            _, current = heapq.heappop(open_list)
            current.expand()

            if current.is_goal(goal_x, goal_y):
                return Node.trace_path(current)

            for child in current.children:
                if child.is_goal(goal_x, goal_y):
                    return Node.trace_path(child)
                if child.location not in visited:
                    heapq.heappush(open_list, (child.f, child))
                    visited[child.location] = True

        return []
