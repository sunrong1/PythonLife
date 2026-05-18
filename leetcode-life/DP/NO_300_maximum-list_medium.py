"""
最长递增子序列


"""

from typing import List

"""
动态规划
定义：
dp[i] 以i为结尾的前i和数的最大连续和

dp[i] = dp[i-1] + nums[i],nums[i]
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        #  most inportant is to define the dp state
        dp = [0] * (len(nums)+ 1)
        # 抢劫i家最大的金钱数目
        dp[0] = 0
        dp[1] = nums[0]
        # 状态转移方程，就是前一家抢和不抢，两者的最大值
        # dp[i] = max(dp[i-2] + nums[i] ,dp[i-1])
        for i in range(2,len(nums)+1):
            dp[i] = max(dp[i-2] + nums[i-1] ,dp[i-1])
        
        
        return dp[len(nums)]


s = Solution();
ss = s.rob([1,2,5])
print("ss:", ss)