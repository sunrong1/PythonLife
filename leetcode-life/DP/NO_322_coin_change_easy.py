"""
最简单的方式：就是使用数学或者叫动态规划

"""

from typing import List

"""
动态规划推导
状态定义：dp[i] 表示金额i的最小硬币数
状态转移：dp[i] = min(dp[i], dp[i-coin]+1) if dp[i-coin] != -1 else dp[i-coin]+1
初始条件：dp[0] = 0
"""






def coinChange(coins: List[int], amount: int) -> int:
    # dp[i] 表示金额i 的最小硬币数
    # 初始化dp[0] = 0
    dp = [-1]* (amount+1)
    dp[0] = 0
    # 遍历所有金额
    for i in range(1,amount+1):
        # 遍历所有硬币
        for coin in coins:
            if i - coin < 0:
                continue
            if dp[i-coin] != -1:
                # 如果dp[i-coin] 不为-1，说明i-coin 可以被组合成，则dp[i] = dp[i-coin]+1
                dp[i] = min(dp[i],dp[i-coin]+1) if dp[i] != -1 else dp[i-coin]+1
    return dp[amount]


print(coinChange([1,2,5],5))
print(coinChange([1,2,5],10))

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp is the number of coins
        dp = [-1] * (amount +1)
        # the amuout = 0,and the number of coins is 0
        dp[0]= 0
        for coin in coins:
            for i in range(1, amount +1):
                if i - coin < 0:
                    continue
                if dp[i-coin] != -1:
                    #  状态转移方程
                    if dp[i] != -1:
                        dp[i] = min(dp[i-coin] +1, dp[i])
                    else:
                        dp[i] = dp[i-coin] +1
        return dp[amount]
    
    def coinChange3(self, coins: List[int], amount: int) -> int:
        # define the state: 凑齐0元需要0个硬币
        dp = [-1]* (amount+1)
        dp[0]=0
        for coin in coins:
            dp[coin] = 1
        
        for i in range(1,amount+1):
            for coin in coins:
                # 防止越界访问
                if i - coin < 0:
                    continue
                
                # 可以组合成这个数量的钱
                if dp[i-coin] != -1:
                    if dp[i] !=-1:
                        # state change formula
                        dp[i] = min(dp[i-coin] +1,dp[i])
                    else:
                        dp[i] = dp[i-coin] + 1
                    
        return dp[amount]
    
s = Solution();
ss = s.coinChange3([1,2,5],6)
print("ss:", ss)