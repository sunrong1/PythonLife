from typing import List

"""
组合综合

方法1
@date : 2022
@update: 2026-5-30
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 路径：数字和为target的-数字组合
        ret = []
        # 可选列表：每层都是一样的
        path = []
        n = len(candidates)
        
        def backtrack(start):
            if sum(path) == target:
                ret.append(path[:])
                return
            if len(path) > 150:
                return
            if sum(path) > target:
                return
            # 可选列表
            # 注意：为了避免重复，只能向后取数据
            for i in range(start, n):
                path.append(candidates[i])
                backtrack(i)
                path.pop()
        
        backtrack(0)
        return ret
    
    # 上面方法的优化：优化反复和运算
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 路径：数字和为target的-数字组合
        ret = []
        # 可选列表：每层都是一样的
        path = []
        n = len(candidates)
        
        def backtrack(start):
           return
        
        backtrack(0)
        return ret
            
s = Solution()
candidates = [2, 3, 6, 7]
print(s.combinationSum(candidates, 7))
    