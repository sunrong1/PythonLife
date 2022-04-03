"""
最简单的方式：就是使用数学或者叫动态规划
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
杨辉三角
"""

"""

有明显的递推关系
dp[0][0]=1
dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
"""

from typing import List

"""
动态规划推导
"""


def generate(numRows: int) -> List[List[int]]:
    dp = [[-1] * numRows for i in range(numRows)]
    ret = []
    for i in range(numRows):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(numRows):
        temp = [1] * (i + 1)
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            temp[j] = dp[i][j]
        temp[i] = 1
        ret.append(temp)
    return ret


"""
简单粗暴的数学
"""


def generate2(numRows: int) -> List[List[int]]:
    ret = list()
    for i in range(numRows):
        row = []
        if i == 0:
            row.append(1)
        for j in range(1, i):
            row.append(ret[i - 1][j - 1] + ret[i - 1][j])
        if i == j:
            row.append(1)
        ret.append(row)
    return ret


print(generate(5))
