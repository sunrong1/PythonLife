"""
岛屿的数量
rid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]

经典的深度优先搜索DFS
1more

"""
from typing import List


def dfs(grid, r, c):
    grid[r][c] = '0'
    row = len(grid)
    col = len(grid[0])
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
            dfs(grid, x, y)


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    row = len(grid)
    col = len(grid[0])
    ret = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                ret += 1
                dfs(grid, r, c)
    return ret


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))
