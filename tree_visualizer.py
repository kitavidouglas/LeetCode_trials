# tree_visualizer.py

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_goal(self, goal_state):
        return self.state == goal_state

def print_solution_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print("\nSolution Path:")
    for p in path:
        print(p)
    return path

def print_tree(node, prefix="", is_last=True):
    print(prefix + ("└── " if is_last else "├── ") + str(node.state))
    prefix += "    " if is_last else "│   "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        print_tree(child, prefix, i == child_count - 1)
