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


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret =[]
        # route 
        path = []
        n = len(nums)
        def trackback(m):
            # 全部选择完，保存结果
            if m == n:
                ret.append(path[:])
                return
            for i in range(m,n):
                # 选择当前路径
                path.append(nums[i])
                trackback(i)
                # 不选择当前路径，两种方式
                path.pop()
         
        trackback(0)
        return ret
s = Solution()
print(s.permute([1, 2]))
