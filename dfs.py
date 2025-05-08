# dfs.py
from state import get_neighbors
from tree_visualizer import TreeNode, print_solution_path, print_tree

def dfs(initial_state, goal_state):
    root = TreeNode(initial_state)
    stack = [root]
    visited = set()

    while stack:
        current_node = stack.pop()
        state = current_node.state
        print(f"Exploring: {state}")

        if state == goal_state:
            print_tree(root)
            return print_solution_path(current_node)

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                child_node = TreeNode(neighbor, current_node)
                current_node.add_child(child_node)
                stack.append(child_node)

    print("No solution found using DFS.")
    return None
