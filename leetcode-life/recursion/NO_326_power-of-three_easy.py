"""
判断是否是3的幂次

递归设计：
初始边界分析：如果= 1，true;  <3 false
递归过程：如果 >=3,每次 除以3，看余数是否是0, 不是就false，否者继续除3 缩小问题

举例：
6
3
1 余数1，返回false
"""


def isPowerOfThree1(n: int) -> bool:
    if n == 1:
        return True
    if n < 3:
        return False

    def divide(n):
        temp1 = n % 3
        if temp1 != 0:
            return False
        temp2 = n // 3
        if temp2 == 1:
            return True
        return divide(temp2)

    return divide(n)


"""
优化程序1：进行边界合并
"""


def isPowerOfThree(n: int) -> bool:
    if n == 1:
        return True
    if n < 3:
        return False
    if n % 3 != 0:
        return False
    return isPowerOfThree(n // 3)


print(isPowerOfThree(6))
print(isPowerOfThree(8))
print(isPowerOfThree(9))


def isPowerOfFour(n: int) -> bool:
    if n == 1:
        return True
    if n < 4:
        return False
    if n % 4 != 0:
        return False
    return isPowerOfFour(n // 4)
