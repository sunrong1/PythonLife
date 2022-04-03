"""
List[List[int]]
"""

"""
矩阵最小和
dp[i][j] 第i行j列的最小和
dp[i][j] = min(dp[i-1][j] ,dp[i][j-1]) + grid[i][j]
d[0][j] = d[0][j-1] +  grid[0][j]
d[i][0] = d[i][0] +  grid[i][0]
"""


def minPathSum(grid) -> int:
    if not grid or len(grid) < 1:
        return 0
    row, col = len(grid), len(grid[0])
    dp = [[0] * col for i in range(row)]
    dp[0][0] = grid[0][0]
    for i in range(1, len(grid)):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, len(grid[0])):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[row - 1][col - 1]


a = [[0, 1], [2, 3], [4, 5]]
minPathSum(a)
