def climbStairs(n: int) -> int:
    sum_step = [0] * (n + 1)
    sum_step[0] = 1
    sum_step[1] = 1
    i = 0
    for i in range(2, n + 1):
        sum_step[i] = sum_step[i - 1] + sum_step[i - 2]
    return sum_step[n]


print(climbStairs(10))
