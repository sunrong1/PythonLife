from typing import List

"""
回溯法
@date: 2026-5-29
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # path ，K 个组合= n的数字
        # 可选列表是 1- 9
        path = []
        ret =[]
        def backtrack(start):
            cursum = sum(path)
            if cursum == n and k == len(path):
                ret.append(path[:])
                return
            if len(path) >= k:
                return
            if cursum >= n:
                return
            
            for i in range(start,10):
                path.append(i)
                backtrack(i+1)
                path.pop()
        
        backtrack(1)
        return ret
        

s = Solution()
print(s.combinationSum3(3,7))
