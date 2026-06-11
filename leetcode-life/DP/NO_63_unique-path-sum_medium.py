
"""
路径和，增加障碍物
@date： 2026-6-11
dp[i][j] 第i行j列的最小和
dp[i][j] = min(dp[i-1][j] ,dp[i][j-1]) + grid[i][j]
d[0][j] = d[0][j-1] +  grid[0][j]
d[i][0] = d[i][0] +  grid[i][0]
"""


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            if obstacleGrid[i][0] ==1:
                break
            dp[i][0] = 1
        for j in range(col):
            if obstacleGrid[0][j] ==1:
                break
            dp[0][j] = 1
        
        for i in range(1,row):
            for j in range(1,col):
                # 跳过障碍物, 更简便的方式，直接把障碍物的位置的步数成0，也可以不作计算
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                # 如果左右两边存在障碍物，就不进行加了那边了
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row-1][col-1]

s = Solution()
ss = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print("ss:", ss)
