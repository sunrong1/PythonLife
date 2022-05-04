"""
省份的数量
实际上是求连通分量
无向图中的极大连通子图称为连通分量
"""
from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    if not isConnected:
        return 0
    visted = set()

    def dfs(isConnected, i):
        for j in range(cities):
            if isConnected[i][j] == 1 and j not in visted:
                visted.add(j)
                dfs(isConnected, j)

    cities = len(isConnected)
    ret = 0
    for i in range(cities):
        if i not in visted:
            ret += 1
            dfs(isConnected, i)
    return ret


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
print(findCircleNum(isConnected))
