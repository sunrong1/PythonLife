import heapq
from typing import List

"""
第K个最大的元素
建立一个小顶堆，只保留K个数，堆顶就是第K大的数
"""


class Solution:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)  # 将num 放入heap中
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


a = [1, 2]
s = Solution(2, a)
c = s.add(3)
print(c)
