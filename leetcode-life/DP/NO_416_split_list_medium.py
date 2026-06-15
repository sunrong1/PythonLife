"""
最简单的方式：就是使用动态规划

"""

from typing import List

"""
动态规划推导,
分割等和子集
@since 2026-6-15
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)% 2 != 0:
            return False
        target = sum(nums) //2
        # 转换成背包问题，0-1背包，不重复，选择出和为target的数字和
        # 实际，回溯算法也可以，但是复杂度比较高
        # 最快的方式拼成target
        
        
        
    
s = Solution();
ss = s.canPartition([1,5,11,5])
print("ss:", ss)