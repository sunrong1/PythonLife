
def climbStairs(n: int) -> int:
    """
    Climbing Stairs problem solution using dynamic programming.
    The function is : dp[i] = dp[i-1] + dp[i-2]
    Args:
        n: An integer representing the number of steps in the staircase.
        
    Returns:
        An integer representing the number of distinct ways to climb to the top.
    """
    if n <= 0:
        return 0
    sum_step = [0] * (n + 1)
    sum_step[1] = 1
    sum_step[2] = 2
    for i in range(3, n + 1):
        sum_step[i] = sum_step[i - 1] + sum_step[i - 2]
    return sum_step[n]


print(climbStairs(10))

def climbStairs2(n: int) -> int:
    """
    method to calculate the number of distinct ways to climb to the top using recursion.

    """
    if n< 1:
        return 0
    if n == 1:
        return 1

    if n == 2:
        return 2

    return climbStairs2(n - 1) + climbStairs2(n - 2)

def climbStairs3(n: int) -> int:
        if n<= 1:
            return 1
        if n == 2:
            return 2
        a =1
        b=2
        for i in range(3,n+1):
            a,b = b,a+b
        return b
