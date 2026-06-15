

"""
路径和，
@date： 2026-6-11
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 到达ij位置路径和
        # 递推公式，分别从左和从上方
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 边上都是1
        dp = [[1 for _ in range(n)] for _ in range(m)]
        # print(dp)
        for i in range(1,m):
            for j in range(1,n):
                # 0 1, 1,0 ==1,1
                # 1 2 <= 0,2 , 1,1
                dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        return dp[m-1][n-1]


s = Solution()
ss = s.uniquePaths(3,3)
print("ss:", ss)
