import heapq
from typing import List

"""
队列中的最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

"""


# 方法1，error，无法保证 保留的是有效的堆顶
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # 创建K个元素的大顶堆
    nums_neg = [-nums[i] for i in range(k)]
    heapq.heapify(nums_neg)

    ans = [-nums_neg[0]]
    # 开始滑动窗口
    for i in range(k, len(nums)):
        heapq.heappush(nums_neg, -nums[i])
        # 只保留有效的堆顶
        if nums_neg[0] == -nums[i - k]:
            heapq.heappop(nums_neg)
        ans.append(-nums_neg[0])
    return ans


# 方法1，error，无法保证 保留的是有效的堆顶
def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
    # 创建K个元素的大顶堆
    nums_neg = [(-nums[i], i) for i in range(k)]
    heapq.heapify(nums_neg)

    ans = [-nums_neg[0][0]]
    # 开始滑动窗口
    for i in range(k, len(nums)):
        heapq.heappush(nums_neg, (-nums[i], i))
        # 只保留有效的堆顶
        while nums_neg[0][1] <= i - k:
            heapq.heappop(nums_neg)
        ans.append(-nums_neg[0][0])
    return ans


a = [1, 3, 1, 2, 0, 5]

b = [-7, -8, 7, 5, 7, 1, 6, 0]
s = maxSlidingWindow(b, 4)
print(s)
