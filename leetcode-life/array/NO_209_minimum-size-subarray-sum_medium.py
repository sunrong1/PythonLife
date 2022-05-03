"""
长度最小的子数组
"""
from typing import List

"""
方法1
暴力解法,双重遍历，效率很低
小优化就是：找到了之后，直接退出
"""


def minSubArrayLen0(target: int, nums: List[int]) -> int:
    if not nums:
        return 0
    l = len(nums) + 1
    for i in range(len(nums)):
        summ = 0
        for j in range(i, len(nums)):
            summ += nums[j]
            if summ >= target:
                l = min(l, (j - i) + 1)
                break
    if l > len(nums):
        return 0
    return l


"""
方法2：
滑动窗口法，记忆过程；
用的非常妙，1more
"""


def minSubArrayLen1(target: int, nums: List[int]) -> int:
    if not nums:
        return 0
    minLen = len(nums) + 1
    l = 0
    r = 0
    summ = nums[l]
    while l <= len(nums) - 1 and r <= len(nums) - 1:
        if summ >= target:
            minLen = min(minLen, r - l + 1)
            summ -= nums[l]
            l += 1
            if summ >= target:
                minLen = min(minLen, r - l + 1)
        else:
            r += 1
            if r <= len(nums) - 1:
                summ += nums[r]
    if minLen > len(nums):
        return 0
    return minLen


nums = [2, 3, 1, 2, 4, 3]
# nums = [2, 3, 4, 3]
# nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
print(minSubArrayLen1(7, nums))
