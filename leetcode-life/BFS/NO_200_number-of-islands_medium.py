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


"""
第二次编写
dfs更加熟悉，编写更加熟练。需要更加明确运动的方向，是四个方向都有可能

DFS：
方向要明确：必须是四个方向搜索，遍历过的设置成0
遍历一次，岛屿加1
递归设计：
停止条件：遇到0返回，否者继续递归搜索
前进：遍历过的设置成0
"""


def numIslands2(grid: List[List[str]]) -> int:
    ret = 0
    if not grid:
        return ret
    row = len(grid)
    col = len(grid[0])

    def dfs(r, c):
        grid[r][c] = '0'
        for (x, y) in [(r + 1, c), [r, c + 1], (r - 1, c), (r, c - 1)]:
            if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                dfs(x, y)

    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                ret += 1
                dfs(r, c)
    return ret


"""
方法2
广度优先搜索
2more
学习了广度优先的写法
设置个队列（使用内置的数据类型，collection，方便许多） 
"""

import collections


def numIslands2_2(grid: List[List[str]]) -> int:
    ret = 0
    if not grid:
        return ret
    row = len(grid)
    col = len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                ret += 1
                grid[r][c] = '0'
                q = collections.deque([(r, c)])
                while q:
                    n, m = q.popleft()
                    for x, y in [(n - 1, m), (n, m - 1), (n + 1, m), (n, m + 1)]:
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                            q.append([x, y])
                            grid[x][y] = '0'
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

# print(numIslands(grid))
# print(numIslands2(grid))
print(numIslands2_2(grid))
