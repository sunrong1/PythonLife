from typing import List

"""
回溯法
@date: 2026-5-28
"""


class Solution:
    # 方法1：不做剪枝，直接取数，到不到长度，自动停止
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        path =[]
        def backtrack(start):
            if len(path) ==k:
                ret.append(path[:])
                return
            # 选择列表，是从1到n
            for i in range(start,n+1):
                path.append(i)
                # 从后面的数据中选择，可以不剪枝
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return ret
    
    # 方法2：方法1上面进行代码优化，进行剪枝
    def combine2(self, n: int, k: int) -> List[List[int]]:
        ret = []
        path =[]
        def backtrack(start):
            if len(path) ==k:
                ret.append(path[:])
                return
              # 剪枝，如何当前path的长度和待加树的长度，达不到结果，直接剪枝
            if k- len(path)  > n - start + 1:
                return
            # 选择列表，是从1到n
            for i in range(start,n+1):
              
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return ret
    # 方法2：方法1上面进行代码优化，进行剪枝
    def combine3(self, n: int, k: int) -> List[List[int]]:
        ret = []
        path =[]
        def backtrack(start):
            if len(path) ==k:
                ret.append(path[:])
                return
              # 剪枝，如何当前path的长度和待加树的长度，达不到结果，直接剪枝
            # if k- len(path)  > n - start + 1:
            #     return
            # 选择列表，是从1到n
            for i in range(start, n -(k - len(path) -2)):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return ret


s = Solution()
print(s.combine2(4,2))
