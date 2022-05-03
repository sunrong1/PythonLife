"""
位运算
计算范围内所有数字的位运算的结果

"""


def rangeBitwiseAnd0(left: int, right: int) -> int:
    ret = right
    for i in range(left, right + 1):
        ret = ret & i
    return ret


"""
算法：
与运算的规律
利用移位运算，进行快速运算
"""


def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    while left < right:
        left = left >> 1
        right = right >> 1
        shift += 1
    return right << shift


l = 5
r = 7
# r = 2147483647
print(rangeBitwiseAnd(l, r))
