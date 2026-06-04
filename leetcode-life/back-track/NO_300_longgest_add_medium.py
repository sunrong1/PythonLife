from typing import List

"""
回溯法;更好的方法是动态规划，回溯法容易超过内存限制
最长递增子序列,严格递增
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 和491类似，先找出所有的递增序列，再找最大的
        path = []
        ret =[]
        n = len(nums)
        def backtrack(start):
            ret.append(path[:])
            used = set()
            for i in range(start,n):
                if path and nums[i] <= path[-1]:
                    continue
                if nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        max_ret  = 0
        for n in ret:
            max_temp = len(n)
            max_ret = max(max_ret,max_temp)
        return max_ret


s = Solution()
print(s.lengthOfLIS([0,1,0,3,2,3]))
