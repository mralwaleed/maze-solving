"""Integration tests for search algorithms."""

import pytest
import numpy as np

from maze_solver.node import Node
from maze_solver.algorithms.bfs import BFS
from maze_solver.algorithms.dfs import DFS
from maze_solver.algorithms.greedy import Greedy
from maze_solver.algorithms.astar import AStar


@pytest.fixture
def corridor_grid():
    """A simple 1x5 horizontal corridor."""
    return np.array([[1, 1, 1, 1, 1]])


@pytest.fixture
def maze_grid():
    """A 7x7 grid with a known path from (0,0) to (6,6).

    1 = open, 0 = wall
    """
    return np.array([
        [1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1],
    ])


class TestBFS:
    def test_finds_path_in_corridor(self, corridor_grid):
        root = Node(0, 0, corridor_grid)
        path = BFS().search(root, 0, 4)
        assert len(path) > 0
        assert path[0].is_goal(0, 4)

    def test_finds_path_in_maze(self, maze_grid):
        root = Node(0, 0, maze_grid)
        path = BFS().search(root, 6, 6)
        assert len(path) > 0
        assert path[0].is_goal(6, 6)

    def test_returns_empty_when_no_path(self):
        grid = np.array([[1, 0, 1]])
        root = Node(0, 0, grid)
        path = BFS().search(root, 0, 2)
        assert path == []

    def test_start_is_goal(self):
        grid = np.array([[1]])
        root = Node(0, 0, grid)
        path = BFS().search(root, 0, 0)
        assert len(path) == 1


class TestDFS:
    def test_finds_path_in_corridor(self, corridor_grid):
        root = Node(0, 0, corridor_grid)
        path = DFS().search(root, 0, 4)
        assert len(path) > 0
        assert path[0].is_goal(0, 4)

    def test_finds_path_in_maze(self, maze_grid):
        root = Node(0, 0, maze_grid)
        path = DFS().search(root, 6, 6)
        assert len(path) > 0
        assert path[0].is_goal(6, 6)

    def test_returns_empty_when_no_path(self):
        grid = np.array([[1, 0, 1]])
        root = Node(0, 0, grid)
        path = DFS().search(root, 0, 2)
        assert path == []


class TestGreedy:
    def test_finds_path_in_maze_manhattan(self, maze_grid):
        root = Node(0, 0, maze_grid, goal_x=6, goal_y=6, heuristic="manhattan")
        path = Greedy().search(root, 6, 6)
        assert len(path) > 0
        assert path[0].is_goal(6, 6)

    def test_finds_path_in_maze_euclidean(self, maze_grid):
        root = Node(0, 0, maze_grid, goal_x=6, goal_y=6, heuristic="euclidean")
        path = Greedy().search(root, 6, 6)
        assert len(path) > 0
        assert path[0].is_goal(6, 6)


class TestAStar:
    def test_finds_optimal_path_in_corridor(self, corridor_grid):
        root = Node(0, 0, corridor_grid, goal_x=0, goal_y=4, heuristic="manhattan")
        path = AStar().search(root, 0, 4)
        assert len(path) > 0
        assert path[0].is_goal(0, 4)

    def test_finds_path_in_maze_manhattan(self, maze_grid):
        root = Node(0, 0, maze_grid, goal_x=6, goal_y=6, heuristic="manhattan")
        path = AStar().search(root, 6, 6)
        assert len(path) > 0
        assert path[0].is_goal(6, 6)

    def test_finds_path_in_maze_euclidean(self, maze_grid):
        root = Node(0, 0, maze_grid, goal_x=6, goal_y=6, heuristic="euclidean")
        path = AStar().search(root, 6, 6)
        assert len(path) > 0
        assert path[0].is_goal(6, 6)
