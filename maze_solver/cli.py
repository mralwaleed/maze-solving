import argparse

from maze_solver.maze_loader import load_maze, draw_path
from maze_solver.node import Node
from maze_solver.algorithms.bfs import BFS
from maze_solver.algorithms.dfs import DFS
from maze_solver.algorithms.greedy import Greedy
from maze_solver.algorithms.astar import AStar


ALGORITHMS = {
    1: ("BFS", BFS, None),
    2: ("DFS", DFS, None),
    3: ("Greedy", Greedy, "manhattan"),
    4: ("A*", AStar, "manhattan"),
}

HEURISTIC_OPTIONS = {
    1: "manhattan",
    2: "euclidean",
}


def run():
    parser = argparse.ArgumentParser(description="Solve a maze using pathfinding algorithms.")
    parser.add_argument("--maze", default="assets/maze.jpg", help="Path to maze image")
    parser.add_argument("--start", nargs=2, type=int, help="Start coordinates: x y")
    parser.add_argument("--goal", nargs=2, type=int, help="Goal coordinates: x y")
    parser.add_argument("--algorithm", type=int, choices=[1, 2, 3, 4],
                        help="1=BFS, 2=DFS, 3=Greedy, 4=A*")
    args = parser.parse_args()

    grid, image = load_maze(args.maze)

    start_x, start_y = args.start if args.start else _prompt_coords("Start")
    goal_x, goal_y = args.goal if args.goal else _prompt_coords("Goal")

    algo_choice = args.algorithm if args.algorithm else _prompt_algorithm()
    name, solver_cls, default_heuristic = ALGORITHMS[algo_choice]

    heuristic = None
    if default_heuristic is not None:
        heuristic = default_heuristic
        if args.algorithm is None:
            heuristic = _prompt_heuristic()

    root = Node(start_x, start_y, grid, goal_x, goal_y, cost=0, heuristic=heuristic)
    solver = solver_cls()
    path = solver.search(root, goal_x, goal_y)

    if not path:
        print("No path found.")
        return

    print(f"Path found using {name}. Path length: {len(path)} nodes.")

    result = draw_path(image, path)
    result.show()


def _prompt_coords(label):
    print(f"{label} position:")
    x = int(input("  X: "))
    y = int(input("  Y: "))
    return x, y


def _prompt_algorithm():
    print("Select algorithm:")
    print("  1 - BFS")
    print("  2 - DFS")
    print("  3 - Greedy Best-First")
    print("  4 - A*")
    while True:
        choice = int(input("Choice: "))
        if choice in ALGORITHMS:
            return choice
        print("Invalid choice. Try again.")


def _prompt_heuristic():
    print("Heuristic function:")
    print("  1 - Manhattan")
    print("  2 - Euclidean")
    while True:
        choice = int(input("Choice: "))
        if choice in HEURISTIC_OPTIONS:
            return HEURISTIC_OPTIONS[choice]
        print("Invalid choice. Try again.")


if __name__ == "__main__":
    run()
