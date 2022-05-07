"""
所有可能路径，有向循环图

"""
from typing import List

"""
方法1
深度优先搜索
递归：
把可能的循环过程写出来，基本的递归过程就抽离出来了
if graph[i] =="" ret.append[temp]

"""


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    ret = []
    if not graph:
        return ret
    n = len(graph)

    def bfs(graph, i, tmp):
        tmp.append(i)
        # if not graph[i]:
        if i == n - 1:
            ret.append(tmp)
            return
        for j in graph[i]:
            tmpj = tmp.copy()
            bfs(graph, j, tmpj)

    tmp = []
    bfs(graph, 0, tmp)
    return ret


graph = [[1, 2], [3], [3], []]
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
graph = [[4, 3, 1], [3, 2, 4], [], [4], []]
# graph = [[2],[],[1]]
print(allPathsSourceTarget(graph))
