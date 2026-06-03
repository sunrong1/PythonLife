from typing import List

"""
回溯法
非递减子序列
"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # path是增加的数字组合数组
        # 可选列表，nums里面的下一个不递减的数字
        path = []
        ret =[]
        n = len(nums)
        if n < 2:
            return ret
        def backtrack(start):
            length = len(path)
            if length>= 2:
                ret.append(path[:])
            
            used = set()
            for i in range(start,n):
                #  分层去重,是关键
                if path and nums[i] < path[-1]:
                    continue
                if nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ret
            

s = Solution()
print(s.findSubsequences([4,4,3,2,1]))
