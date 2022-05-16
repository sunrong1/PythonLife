from typing import List

"""
子集II
方法1 DFS
递归
停止条件 base condition: i 到最后一个
前进段：加入ret中
后退段：无

方法2：
回溯法
1more
"""


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    ret = [[]]
    if not nums:
        return ret

    def dfs(i, tmp):
        while i < len(nums):
            t = tmp.copy() + [nums[i]]
            if ret.count(t) > 0:
                i += 1
                continue
            else:
                ret.append(t)
            dfs(i + 1, tmp + [nums[i]])
            i += 1

    nums.sort()
    dfs(0, [])
    return ret


nums = [1, 2, 2]
print(subsetsWithDup(nums))
