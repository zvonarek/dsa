#ll are graphs and so are BT
#edges <= nodes^2 (=vertix^2)
#represent as a matrix, adj matrix, or adj list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
#Matirx DFS
#Count the unique paths from the top left to the bottom right
#a single path may only move along 0's and cannot visit the same cell > one time
#ex. of backtracking 
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1: return 1

    visit.add((r,c))
    count = 0 
    count += dfs(grid,r+1,c,visit)
    count += dfs(grid,r-1,c,visit)
    count += dfs(grid,r,c+1,visit)
    count += dfs(grid,r,c-1,visit)
    visit.remove((r,c))
    return count
print(dfs(grid,0,0,set()))

#LC 200 Number of Islands
def numIslands(self,grid:list[list[str]])-> int:
    #add code.
