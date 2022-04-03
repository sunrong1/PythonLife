"""
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

4 -1 1 2 -2
含义定义要清晰 ！！！！
迭代过程：
1. 当前数是最大值：
2. 当前的和数最大；


"""

from typing import List

"""
动态规划
定义：
dp[i] 以i为结尾的前i和数的最大连续和

dp[i] = dp[i-1] + nums[i],nums[i]
"""


def maxSubArray(nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
