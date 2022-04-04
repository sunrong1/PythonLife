"""
x > 0场景
sum= x
sum = x * x *x
sum(n-1) *x

x< 0场景：

"""


def myPow(x: float, n: int) -> float:
    num = n if n > 0 else -n

    def calPow(x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        return x * myPow(x, n - 1)

    sum = 0
    if n > 0:
        sum = calPow(x, n)
    else:
        sum = 1 / calPow(x, num)
    return sum


"""
优化方法1：
使用分治法

x**4 == x**2 X x**2
x**5 == x**2 X x**2 X x
"""


def myPow1(x: float, n: int) -> float:
    num = n if n > 0 else -n

    def calPow(x, n):
        if n == 0:
            return 1
        y = calPow(x, n // 2)
        if n % 2 == 0:
            return y * y
        else:
            return y * y * x

    sum = 0
    if n > 0:
        sum = calPow(x, num)
    else:
        sum = 1 / calPow(x, num)
    return sum


print(myPow1(2, 2147483647))
