"""Unit tests for the Node class."""

import pytest
import numpy as np

from maze_solver.node import Node


@pytest.fixture
def simple_grid():
    return np.array([
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1],
    ])


@pytest.fixture
def open_grid():
    return np.ones((5, 5), dtype=int)


class TestNodeInit:
    def test_basic_node_has_no_heuristic(self, simple_grid):
        node = Node(0, 0, simple_grid)
        assert node.h == 0
        assert node.cost == 0
        assert node.f == 0

    def test_manhattan_heuristic(self, simple_grid):
        node = Node(0, 0, simple_grid, goal_x=2, goal_y=2, heuristic="manhattan")
        assert node.h == 4

    def test_euclidean_heuristic(self, simple_grid):
        node = Node(0, 0, simple_grid, goal_x=3, goal_y=4, heuristic="euclidean")
        assert node.h == 5

    def test_f_is_cost_plus_heuristic(self, simple_grid):
        node = Node(0, 0, simple_grid, goal_x=2, goal_y=0, cost=5, heuristic="manhattan")
        assert node.f == 7


class TestNodeGoal:
    def test_is_goal_true(self, simple_grid):
        node = Node(2, 2, simple_grid)
        assert node.is_goal(2, 2) is True

    def test_is_goal_false(self, simple_grid):
        node = Node(0, 0, simple_grid)
        assert node.is_goal(2, 2) is False


class TestNodeExpansion:
    def test_expand_on_open_grid(self, open_grid):
        root = Node(2, 2, open_grid)
        root.expand()
        assert len(root.children) == 4

    def test_expand_blocked_directions(self, simple_grid):
        # Node at (1,1) — can only go up (0,1) or down (2,1)
        node = Node(1, 1, simple_grid)
        node.expand()
        assert len(node.children) == 2

    def test_corner_node_expansion(self, simple_grid):
        # Top-left corner (0,0) — can go right (0,1) only (down is 0)
        node = Node(0, 0, simple_grid)
        node.expand()
        assert len(node.children) == 1
        assert node.children[0].x == 0
        assert node.children[0].y == 1

    def test_child_has_parent_set(self, open_grid):
        root = Node(2, 2, open_grid)
        root.expand()
        for child in root.children:
            assert child.parent is root

    def test_child_cost_increments(self, open_grid):
        root = Node(2, 2, open_grid, cost=3)
        root.expand()
        for child in root.children:
            assert child.cost == 4


class TestTracePath:
    def test_trace_single_node(self, simple_grid):
        node = Node(0, 0, simple_grid)
        path = Node.trace_path(node)
        assert len(path) == 1
        assert path[0] is node

    def test_trace_chain(self, open_grid):
        root = Node(0, 0, open_grid)
        root.expand()
        child = root.children[0]
        path = Node.trace_path(child)
        assert len(path) == 2
        assert path[0] is child
        assert path[1] is root
