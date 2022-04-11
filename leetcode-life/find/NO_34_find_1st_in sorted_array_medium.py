from typing import List

"""
算法设计
先二分查找到目标，然后遍历首位，获取最小 最大的index

边界分析：
首尾比较，排查边界，获取最大和最小的index
中间位置，如果查找到，开始左右遍历,找到序号的极限位置

"""


def searchRange(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]
    length = len(nums)
    if length < 1 or nums[0] > target or nums[length - 1] < target:
        return result
    mid = length // 2
    start = 0
    end = length - 1
    while start <= end:
        if nums[mid] < target:
            start = mid + 1
            # mid = mid + 1 + (end - mid - 1) // 2
            # 优化公式
            mid = (start + end) // 2
        elif nums[mid] > target:
            end = mid - 1
            # mid = start + (mid - 1 - start) // 2
            # 优化计算
            mid = (start + end) // 2
        else:
            break
    if nums[mid] != target:
        return result
    start = mid
    end = mid
    while start >= 0 and nums[start] == target:
        start -= 1
    while end < length and nums[end] == target:
        end += 1

    return [start + 1, end - 1]


nums = [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 4]
print(searchRange(nums, 3))
