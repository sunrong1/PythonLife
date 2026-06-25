"""
最简单的方式：就是使用动态规划

"""

from typing import List

"""
动态规划推导,
分割等和子集
@since 2026-6-15

动规五部曲：
        # dp[i] ,含义
        # dp[i] = ..状态转移方程
        # dp[0] 初始化
        # 遍历顺序
        # 打印dp数组

"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums)% 2 != 0:
            return False
        # 凑成就可以，装满容量为target的背包
        target = sum(nums) //2
        # 转换成背包问题，0-1背包，不重复，选择出和为target的数字和
        # 实际，回溯算法也可以，但是复杂度比较高
        # 最快的方式拼成target
        # dp[i] ===》容量为i的为i的背包，最大价值，价值和重量是相同
        # dp[i] = max( dp[j] ,dp[j] + dp[j-w[i]] +v[i])
        # dp[0] 初始化
        # 遍历顺序
        # 打印dp数组
        dp = [0] * (target+1)
        dp[0] = 0
        for i in range(n):
            for j in range(target,i+1,-1):
                return
            
    def canPartition0(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums)% 2 != 0:
            return False
        # 凑成就可以，装满容量为target的背包
        target = sum(nums) //2
        # 转换成背包问题，0-1背包，不重复，选择出和为target的数字和
        # 实际，回溯算法也可以，但是复杂度比较高
        # 最快的方式拼成target
        # dp[i] ===》容量为i的为i的背包，最大价值，价值和重量是相同
        # dp[i] = max( dp[j] ,dp[j] + dp[j-w[i]] +v[i])
        # dp[0] 初始化
        # 遍历顺序
        # 打印dp数组
        dp = [[False] for _ in range(n) for _ in range(target+1)] 
        # dp[0] = 0
        # 第一行初始化
        for i in range(n):
            dp[0][nums[i]] == True
        for i in range(1,n):
            for j in range(target+1):
                if dp[i-1][j] == True:
                    dp[i][j] == True
                if dp[]
        
        
        
    
s = Solution();
ss = s.canPartition([1,5,11,5])
print("ss:", ss)