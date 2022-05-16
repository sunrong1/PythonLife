"""
矩阵中最短路径

"""
from typing import List

"""
问题理解：
固定方向：从左上角，走到右下脚
路径可能右多个，取最小的一个
1more
方法1：
深度优先搜索，可能会超时
所有可能路径全部找出，取最小的路径
递归设计：
停止条件：前面没有路，直接返回；前面的路，是终点，加到path，返回
前进段：走所有可能的0路径，上下左右，四个方向都要判断下
后退段：无

方法2:
广度优先搜索
第一个到达终点的就是最短的路径
广度优先搜索，有queue
每走一步，同时向八个方向走，先走到终点的就是最短路径


"""


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if not grid:
        return -1
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    queue = [(0, 0, 1)]
    # 广度搜索 队列中
    for (x, y, count) in queue:
        if (x == n - 1) and y == n - 1:
            return count
        # 八个方向搜索
        for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1),
                       (x + 1, y - 1)]:
            # 条件符合的，加入队列，进行待遍历状态
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                queue.append((i, j, count + 1))

    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))
