from typing import List

"""
回溯法
最长递增子序列,严格递增
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        path = []


s = Solution()
print(s.lengthOfLIS("aab"))
