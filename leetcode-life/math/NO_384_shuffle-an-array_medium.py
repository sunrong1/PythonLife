"""
打乱数组运算

"""
import random
from typing import List

"""
方法1：
直接使用random中的shuffle函数
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.originNums = nums.copy()

    def reset(self) -> List[int]:
        return self.originNums

    def shuffle(self) -> List[int]:
        self.nums = self.originNums.copy()
        random.shuffle(self.nums)
        return self.nums


"""
方法2：
使用random.randrange方法实现
"""


class Solution0:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.originNums = nums.copy()

    def reset(self) -> List[int]:
        return self.originNums

    def shuffle(self) -> List[int]:
        ret = [0] * len(self.originNums)
        for i in range(len(self.originNums)):
            j = random.randrange(len(self.nums))
            ret[i] = self.nums.pop(j)

        self.nums = ret
        return self.nums


n = [1, 2, 3]
s = Solution0(n)
print(s.shuffle())
print(s.reset())
print(s.shuffle())
