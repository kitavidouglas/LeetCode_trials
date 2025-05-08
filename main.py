# main.py

from collections import deque
from state import get_neighbors, is_valid
from bfs import bfs
from dfs import dfs

ENTITY_NAMES = ["Man", "Leopard", "Goat", "Grass"]

def describe_state(state):
    left  = [ENTITY_NAMES[i] for i,v in enumerate(state) if v==0]
    right = [ENTITY_NAMES[i] for i,v in enumerate(state) if v==1]
    return f"[L:{','.join(left):<10}|R:{','.join(right)}]"

class BinNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

def build_binary_view(path):
    pruned_map = {}
    for i in range(len(path)-1):
        cur, nxt = path[i], path[i+1]
        pruned_map[cur] = [n for n in get_neighbors(cur) if n!=nxt]

    root = BinNode(describe_state(path[0]))
    cursor = root
    for i in range(len(path)-1):
        cur, nxt = path[i], path[i+1]
        sibs = pruned_map[cur]
        if sibs:
            sib_labels = " , ".join(describe_state(s) for s in sibs)
            cursor.left = BinNode(f"[PRUNED {len(sibs)}: {sib_labels}]")
        else:
            cursor.left = BinNode("[PRUNED 0]")
        cursor.right = BinNode(describe_state(nxt))
        cursor = cursor.right
    return root

def print_slash_tree(node, indent=""):
    print(indent + node.label)
    if node.left or node.right:
        mid = len(indent) + len(node.label)//2
        line = [" "] * (mid + 2)
        if node.left:  line[mid-1] = "/"
        if node.right: line[mid+1] = "\\"
        print("".join(line))
        child_indent = indent + "    "
        if node.left:  print_slash_tree(node.left,  child_indent)
        if node.right: print_slash_tree(node.right, child_indent)

def describe_steps(path, algo):
    print(f"\n--- {algo} Step-by-Step ---")
    for i in range(len(path)-1):
        cur, nxt = path[i], path[i+1]
        print(f"\nStep {i+1}: State {describe_state(cur)}")
        moves = get_neighbors(cur)
        for m in moves:
            mark = "→" if m==nxt else "✗"
            print(f"   {mark} {describe_state(m)}")
        left = [ENTITY_NAMES[j] for j,v in enumerate(cur) if v==0]
        right= [ENTITY_NAMES[j] for j,v in enumerate(cur) if v==1]
        print(f"   Banks: Left={left}, Right={right}")
    print(f"\nReached goal {describe_state(path[-1])}\n")

def record_bfs_visits(initial, goal):
    visited, order = set(), []
    queue = deque([initial])
    while queue:
        s = queue.popleft()
        if s in visited: continue
        visited.add(s); order.append(s)
        if s==goal: break
        for n in get_neighbors(s):
            if n not in visited: queue.append(n)
    return order

def record_dfs_visits(initial, goal):
    visited, order = set(), []
    def _dfs(s):
        if s in visited: return False
        visited.add(s); order.append(s)
        if s==goal: return True
        for n in get_neighbors(s):
            if _dfs(n): return True
        return False
    _dfs(initial)
    return order

def print_truth_table(initial, goal, bfs_path, dfs_path):
    bfs_vis = record_bfs_visits(initial, goal)
    dfs_vis = record_dfs_visits(initial, goal)
    states = [(m,l,g,gr) for m in [0,1] for l in [0,1]
                           for g in [0,1] for gr in [0,1]]

    # Build rows
    rows = []
    for st in states:
        rows.append({
            'State':      str(st),
            'Valid':      str(is_valid(st)),
            'Neighbors':  str(get_neighbors(st)),
            'BFS_Order':  str(bfs_vis.index(st)+1) if st in bfs_vis else "",
            'In_BFS':     "Yes" if st in bfs_path else "No",
            'DFS_Order':  str(dfs_vis.index(st)+1) if st in dfs_vis else "",
            'In_DFS':     "Yes" if st in dfs_path else "No",
        })

    # Compute column widths
    cols = ['State','Valid','Neighbors','BFS_Order','In_BFS','DFS_Order','In_DFS']
    widths = {c:max(len(c), *(len(r[c]) for r in rows)) for c in cols}

    # Header
    header = " | ".join(c.ljust(widths[c]) for c in cols)
    sep    = "-+-".join("-"*widths[c] for c in cols)
    print("\n=== Truth Table of All 16 States ===\n")
    print(header)
    print(sep)
    for r in rows:
        line = " | ".join(r[c].ljust(widths[c]) for c in cols)
        print(line)
    print()

if __name__ == "__main__":
    initial = (0,0,0,0)
    goal    = (1,1,1,1)

    # BFS
    print("\n=== BFS Binary-Tree View ===\n")
    bfs_path = bfs(initial, goal)
    if bfs_path:
        bfs_root = build_binary_view(bfs_path)
        print_slash_tree(bfs_root)
        describe_steps(bfs_path, "BFS")
        print("Explanation (BFS): BFS explores level by level, halting when the goal is dequeued;")
        print("remaining siblings/deeper nodes are pruned (left branches).\n")
        print(" • BFS explores all nodes at each depth before going deeper.")
        print(" • It halts the moment the goal is dequeued, so siblings at that level and deeper")
        print("   are pruned (shown in left branches).\n")
    else:
        print("No BFS solution.\n")

    # DFS
    print("\n=== DFS Binary-Tree View ===\n")
    dfs_path = dfs(initial, goal)
    if dfs_path:
        dfs_root = build_binary_view(dfs_path)
        print_slash_tree(dfs_root)
        describe_steps(dfs_path, "DFS")
        print("Explanation (DFS): DFS dives one path to the goal, never backtracking;")
        print("all non-chosen siblings appear as pruned left branches.\n")
        print(" • DFS plunges down one branch until the goal is reached.")
        print(" • It never backtracks to explore siblings, so all non-taken moves appear as pruned.\n")
    else:
        print("No DFS solution.\n")

    # Truth table
    print_truth_table(initial, goal, bfs_path or [], dfs_path or [])
