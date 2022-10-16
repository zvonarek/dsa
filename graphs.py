#ll are graphs and so are BT
#edges <= nodes^2 (=vertix^2)
#represent as a matrix, adj matrix, or adj list

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

