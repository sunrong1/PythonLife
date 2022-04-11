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


def permute1(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

    backtrack(nums, [])
    return res


print(permute([1, 2]))
