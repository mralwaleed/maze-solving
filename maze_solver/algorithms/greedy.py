import heapq

from maze_solver.node import Node


class Greedy:
    """Greedy Best-First Search — expands the node with the lowest heuristic value.

    Fast, but does not guarantee the optimal path.
    """

    def search(self, root, goal_x, goal_y):
        open_list = []
        heapq.heappush(open_list, (root.h, root))
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
                    heapq.heappush(open_list, (child.h, child))
                    visited[child.location] = True

        return []
