from typing import List

"""
回溯法
@date: 2026-5-28
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        path =[]
        def backtrack(start):
            if len(path) ==k:
                ret.append(path[:])
                return
            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return ret


s = Solution()
print(s.combine(4,2))
