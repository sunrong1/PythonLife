

"""
不同的二叉搜索树

"""


class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] i数组成的二叉搜索树有多少种
        dp = [0] *(n+1)        
        dp[0] =1
        dp[1] =1
        # dp[2]= 2
        # 1开头
        # dp[3] = 2+ 1+ 2 =5 = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
        # dp[4] = dp[1]
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] =dp[i] + dp[j-1] * dp[i-j]
        return dp[n]

s = Solution()
ss = s.numTrees(3)
print("ss:", ss)
