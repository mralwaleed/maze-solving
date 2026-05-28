# Maze Solver

Python implementation of four pathfinding algorithms applied to image-based mazes. Loads a maze from a grayscale image, converts it into a binary grid, and solves it using BFS, DFS, Greedy Best-First, or A*. The solved path is drawn directly onto the image.

Built as an AI course project to demonstrate how search algorithms handle robot path planning — finding optimal or near-optimal routes through obstacle grids the same way autonomous systems do.

## Prerequisites

- Python 3.9+
- pip

## Tech Stack

- **Python 3** — core language
- **NumPy** — binary grid representation of the maze
- **Pillow (PIL)** — image loading, pixel manipulation, and display
- **pytest** — test runner

## Installation

```bash
# Clone the repo
git clone https://github.com/mralwaleed/maze-solving.git
cd maze-solving

# Install dependencies
pip install -r requirements.txt

# Or install as an editable package (includes dev dependencies)
pip install -e ".[dev]"
```

## Running

**Interactive mode** (prompts for start/goal positions and algorithm choice):

```bash
python3 main.py
```

**CLI mode** (pass everything as arguments):

```bash
python3 main.py --maze assets/maze.jpg --start 10 10 --goal 200 200 --algorithm 4
```

Algorithm options: `1` = BFS, `2` = DFS, `3` = Greedy, `4` = A*.

The program opens a window showing the maze with the solved path highlighted.

## Project Structure

```
maze-solving/
├── main.py                       # Entry point
├── pyproject.toml                # Package config
├── requirements.txt              # Dependencies
├── assets/
│   └── maze.jpg                  # Sample maze image
├── maze_solver/
│   ├── __init__.py
│   ├── cli.py                    # CLI interface and argument parsing
│   ├── maze_loader.py            # Image → grid conversion, path drawing
│   ├── node.py                   # Unified node class (heuristic-aware)
│   └── algorithms/
│       ├── __init__.py
│       ├── astar.py              # A* search
│       ├── bfs.py                # Breadth-first search
│       ├── dfs.py                # Depth-first search
│       └── greedy.py             # Greedy best-first search
├── tests/
│   ├── __init__.py
│   ├── test_node.py              # Node unit tests
│   └── test_algorithms.py        # Algorithm integration tests
├── results/                      # Saved output images
│   ├── A_Star_Manhattan.png
│   ├── BFS.png
│   ├── DFS.png
│   └── Greedy_Manhattan.png
└── readme.md
```

## Algorithms

| Algorithm | Guarantees Shortest Path | Uses Heuristic | Strategy |
|-----------|--------------------------|----------------|----------|
| BFS       | Yes                      | No             | Explores all nodes at current depth before going deeper |
| DFS       | No                       | No             | Explores as deep as possible before backtracking |
| Greedy    | No                       | Yes            | Always picks the node closest to the goal |
| A*        | Yes                      | Yes            | Balances actual cost + heuristic for optimal path |

Greedy and A* support two heuristic functions:
- **Manhattan distance** — `|dx| + |dy|`, suited for grids with 4-directional movement
- **Euclidean distance** — `sqrt(dx² + dy²)`, straight-line distance to goal

## Running Tests

```bash
python3 -m pytest tests/ -v
```

This runs 25 tests covering node creation, expansion, heuristic calculation, path tracing, and all four algorithms against known grids.

## Results

All algorithms tested against the same maze image:

**A\* (Manhattan)** — optimal path, cost-aware:

![A* Manhattan](https://github.com/mralwaleed/maze-solving/blob/gh-pages/Result/A_Star_Manhattan.png)

**Greedy (Manhattan)** — fast but not always optimal:

![Greedy Manhattan](https://github.com/mralwaleed/maze-solving/blob/gh-pages/Result/Greedy_Manhattan.png)

**BFS** — guarantees shortest path, explores more nodes:

![BFS](https://github.com/mralwaleed/maze-solving/blob/gh-pages/Result/BFS.png)

**DFS** — fast but path quality varies:

![DFS](https://github.com/mralwaleed/maze-solving/blob/gh-pages/Result/DFS.png)

## Roadmap

Planned improvements for future iterations:

1. **Web-based visualization** — Replace the CLI image viewer with a browser UI (Flask + Canvas or Matplotlib animation) that renders the maze and animates the search in real time, showing explored nodes and the final path step by step. The entry point would be `maze_solver/server.py`, serving a static frontend that communicates with the solver via a REST endpoint.

2. **Maze generator** — Add a procedural maze generator (`maze_solver/generator.py`) using recursive backtracking or Prim's algorithm. This removes the dependency on external maze images and makes the project self-contained for testing and demos. Generated mazes would be saved as images in `assets/`.

3. **Algorithm comparison mode** — Run all four algorithms on the same maze and display a side-by-side comparison of path length, nodes explored, and execution time. This would live in `maze_solver/benchmark.py` and could output a summary table or comparison image.
