"""
最简单的方式：就是使用数学或者叫动态规划

"""

from typing import List

"""
动态规划推导
找找到核心解题思路，发现和动态规划的思想比较吻合
二维表，手动绘制解题思路，动态规划的过程

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 行，列
        m  = len(text1)
        n = len(text2)
        # dp[i][j] 前i j个字符匹配的最大量
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 初始化边界
        # for i in range(0,len(text1) +1):
        #     dp[i][0] = 0
        # for j in range(0,len(text2) +1):
        #     dp[0][j] = 0
        
        for i in range(1,len(text1)+ 1):
            for j in range(1,len(text2) +1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 不增加，但是取左边或者上边矩阵的最大值
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
    
s = Solution()
ss = s.longestCommonSubsequence("abc","abd")
print("ss:", ss)