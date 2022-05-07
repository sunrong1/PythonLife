"""
矩阵中最短路径

"""
from typing import List

"""
问题理解：
固定方向：从左上角，走到右下脚
路径可能右多个，取最小的一个

方法1：
深度优先搜索
所有可能路径全部找出，取最小的路径
递归设计：
停止条件：前面没有路，直接返回；前面的路，是终点，加到path，返回
前进段：走所有可能的0路径，上下左右，四个方向都要判断下
后退段：无
"""


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if not grid:
        return -1
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    allpath = []
    