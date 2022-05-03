from typing import List

"""
方法1
比较经典的滑动窗口的题目
用滑动窗口方法，寻找规律,连续的子集
1more
"""


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if not nums:
        return 0
    if k <= 0:
        return 0
    ret = 0
    l = 0
    r = 0
    summ = 1
    while r <= len(nums) - 1:
        summ = summ * nums[r]
        while l <= r and summ >= k:
            summ = summ // nums[l]
            l += 1
        if r >= l:
            ret += r - l + 1
            # print(r)
            # print("个数：" + str(r - l + 1))
        r += 1
    return ret


nums = [10, 5, 2, 6]
print(numSubarrayProductLessThanK(nums, 100))
