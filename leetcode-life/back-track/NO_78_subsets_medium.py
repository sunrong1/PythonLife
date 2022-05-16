"""
数组的所有子集
"""
from typing import List

"""
问题理解：
求所有可能路径，
不包含重复的子集
1more
方法1
深度优先搜索
不包含重复的子集
要求后面的index大于前面的index

递归：
停止条件：index到尾部了，
递归一次，返回序列扩大一次；
前进段：不断增加返回值序列
后退段：空

"""


def subsets(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    ret = [[]]
    length = len(nums)

    # 第一次递归：1 2 3 加入结果
    # 第二次递归
    def dfs(i, tmp: List[int]):
        while i <= length - 1:
            ret.append(tmp + [nums[i]])
            dfs(i + 1, tmp + [nums[i]])
            i += 1

    dfs(0, [])
    return ret


"""
方法2：
广度优先搜索

"""


def subsets0(nums: List[int]) -> List[List[int]]:
    ret = [[]]
    if not nums:
        return ret
    q = [nums[0]]


nums = [1, 2, 3]
print(subsets(nums))
