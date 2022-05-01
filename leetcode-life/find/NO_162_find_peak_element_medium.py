from typing import List

"""
寻找峰值
这是一道严格的数学证明题；

"""

"""
方法
算法设计：
规律，对于任意相邻元素步等的数组，要么在上坡中，要么在下坡中，顺着坡就可以找到峰值

二分法：
寻找可能的峰值点：
中间m，m+1大，就往右走；
否者左边大，往左走；
否者返回这个m
"""


def findPeakElement(self, nums: List[int]) -> int:
    if not nums:
        return -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if m + 1 <= len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        elif m - 1 >= 0 and nums[m] < nums[m - 1]:
            r = m - 1
        else:
            return m
    return l


nums = [1, 2]
print(findPeakElement("", nums))
