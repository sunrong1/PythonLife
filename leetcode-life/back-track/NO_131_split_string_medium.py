from typing import List

"""
回溯法
切割问题
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # think the path and slect
        # a aa aab
        # a ab
        # b
        path =[]
        ret =[]
        n = len(s)
        def backtrack(i):
            # collect the result
            if i == n:
                ret.append(path[:])
                return 
            for i in range(n):
                continue


s = Solution()
print(s.partition("aab"))
