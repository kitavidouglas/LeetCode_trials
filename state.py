# state.py

def is_valid(state):
    """Check if a state is valid (no eating)."""
    M, L, G, Gr = state
    
    # Unsafe conditions: Leopard eats Goat or Goat eats Grass
    if (L == G and M != L):  # Man not present, leopard eats goat
        return False
    if (G == Gr and M != G):  # Man not present, goat eats grass
        return False
    return True

def get_neighbors(state):
    """Generate valid next moves."""
    M, L, G, Gr = state
    moves = []
    
    possible_moves = [
        (1, 0, 0, 0),  # Man alone
        (1, 1, 0, 0),  # Man + Leopard
        (1, 0, 1, 0),  # Man + Goat
        (1, 0, 0, 1)   # Man + Grass
    ]
    
    for move in possible_moves:
        new_state = (M ^ 1, L ^ move[1], G ^ move[2], Gr ^ move[3])  # Flip only chosen ones
        
        if is_valid(new_state) and new_state != state:  # Avoid reversing the move
            moves.append(new_state)
            print(f"Valid Move: {state} -> {new_state}")  # Debugging Output
    
    return moves

