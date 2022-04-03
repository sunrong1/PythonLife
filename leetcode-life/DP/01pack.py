"""
有N件物品和一个最多能被重量为W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。

	重量	价值
物品0	1	15
物品1	3	20
物品2	4	30

pack = 4kg 总价值如何装最大？

初始化DP数组含义，dp[i][j],表示从0~i个物品中任意挑选放到j容量包里面的最大价值

推导公式（状态转移方程），即放入i物品和不放入的最大值
dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w(i)] + v(i))
"""

from typing import List


def pack(nums, weight):
    dp = [[0] * (weight + 1) for i in range(len(nums))]

    # 初始条件,0个物品，放入j容量的袋子，最大价值，因为只能放一个，所以就是0 物品的价值
    for i in range(nums[0][0], weight + 1):
        dp[0][i] = nums[0][1]

    # 状态转移方程，i是物品,j是容量
    for i in range(1, len(nums)):
        for j in range(weight + 1):
            # 放不开的场景，和放的开的场景
            if j < nums[i][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i][0]] + nums[i][1])
    return dp[len(nums) - 1][weight]


nums = [(1, 15), (3, 20), (4, 30)]
print(pack(nums, 4))
