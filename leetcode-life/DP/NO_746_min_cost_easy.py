"""
最简单的方式：就是使用数学或者叫动态规划

"""

from typing import List

"""
动态规划推导
找找到核心解题思路，发现和动态规划的思想比较吻合
爬楼梯的最小花费, 一定要把dp[i]物理含义想清楚

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] 走到最顶层i的最小花费
        n = len(cost)
        # dp[n] = min(dp[i-1],dp[i-2])
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0]= 0
        dp[1] = 0
        # 从0 跨2步直接上，从1直接上去
        dp[2] = min(cost[0],cost[1])
        # 从1的位置上，从2号位置上
        # dp[3] = min(dp[1] + cost[1],dp[2]+ cost[2])
        for i in range(3,n+1):
            dp[i] = min(dp[i-2]+ cost[i-2],dp[i-1] + cost[i-1])
        return dp[n]
    
s = Solution()
ss = s.minCostClimbingStairs([10,15,20])
print("ss:", ss)