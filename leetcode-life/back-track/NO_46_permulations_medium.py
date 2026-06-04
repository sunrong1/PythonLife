from typing import List

"""
全排列场景，回溯法最合适

递归设计：

子问题分解展开图：先用第一个递归遍历，再用第二个数递归遍历；展开遍历的条件都是一样的‘
遍历过程中,不断缩小遍历元素的范围
边界分析：
"""


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def track(r: List, tmp):
        if not r:
            result.append(tmp)
            return
        for i in range(len(r)):
            track(r[:i] + r[i + 1:], tmp + [r[i]])

    track(nums, [])
    return result

"""_summary_
回溯法全排列
@since 2021
@update 2026-6
Returns:
    _type_: _description_
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path =[]
        ret =[]
        n = len(nums)
        
        def backtrack(used):
            if len(path) == n:
                ret.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(used)
                used[i] = 0
                path.pop()
        backtrack([0] * n)
        return ret
    
    def permute0(self, nums: List[int]) -> List[List[int]]:
        path =[]
        ret =[]
        n = len(nums)
        
        def backtrack():
            if len(path) == n:
                ret.append(path[:])
                return
            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack()
                path.pop()
        backtrack()
        return ret
    
    
s = Solution()
print(s.permute([1, 2, 3]))
