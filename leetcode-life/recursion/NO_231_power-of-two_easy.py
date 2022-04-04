"""
判断是否是2的幂次

递归设计：
初始边界分析：如果= 1 or =2，true;  <1 false
递归过程：如果 >=2,每次 除以2，看余数是否是0, 不是2 就false，否者继续除

举例：
6
3
1 余数1，返回false
"""


def isPowerOfTwo(n: int) -> bool:
    if n < 1:
        return False
    if n == 1:
        return True

    def divide(n):
        temp1 = n % 2
        if temp1 != 0:
            return False
        temp2 = n // 2
        if temp2 == 1:
            return True
        return divide(temp2)

    return divide(n)


print(isPowerOfTwo(6))
print(isPowerOfTwo(8))
