from typing import List

"""
全排列
方法1
回溯算法
1more
递归设计

"""


def permuteUnique(nums: List[int]) -> List[List[int]]:
    res = []
    if not nums:
        return res
    used = [0] * len(nums)

    def backtracking(path):
        # base condition 停止条件
        if len(path) == len(nums):
            res.append(path.copy())
            return

        for i in range(len(nums)):
            # 深度优先遍历，当前i没有使用过
            if not used[i]:
                # 剪枝去重，used[i-1]==false 当前树枝没有使用过，==true，当前树枝使用过
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtracking(path)
                # 回溯，换另外一个数
                path.pop()
                used[i] = 0

    nums.sort()
    backtracking([])
    return res


nums = [1, 1, 2]
print(permuteUnique(nums))
