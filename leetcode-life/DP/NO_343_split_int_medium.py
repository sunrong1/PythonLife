"""
最简单的方式：就是使用动态规划

"""

from typing import List

"""
动态规划推导
整数拆分
"""






class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] i 被拆后最大的结果,记住是被拆后，不包含原数
        # dp[i] = 1* dp[i-1]or 2 * dp[i-2]
        dp = [0] * (n+1)
        dp[1] =1
        dp[2] =1
        # dp[3] =2 
        for i in range(3,n+1):
            end = i // 2
            for j in range(1,end +1):
                # 分两种情况，拆和不拆
                dp[i] = max(j * dp[i-j],j*(i-j),dp[i])
        print(dp)
        return dp[n]
        
    
s = Solution();
ss = s.integerBreak(6)
print("ss:", ss)