from typing import List

"""
 输入：A = [2, 1, 0], B = [], C = []
 输出：C = [2, 1, 0]
"""

"""
递归设计：
子问题设计：A取最小，即最后一个-》B上, C全部--》B上 B全部-->C 的设计流程
边界条件：A为空结束

前进段：A取最小，即最后一个-》B上, C全部--》B上 B全部-->C
后退段：不做啥
"""


def hanota(A: List[int], B: List[int], C: List[int]) -> None:
    if not A:
        return
    B.append(A[-1])
    for item in C:
        B.append(item)
    C.clear()
    # C = [] 不能这么写！！！！会重新定义外部C的地址，和外部进行失联
    for item in B:
        C.append(item)
    B.clear()
    A.pop()
    # print(C)
    hanota(A, B, C)


A = [i for i in range(200, 1, -1)]
B = list()
C = list()
print(A)
hanota(A, B, C)
print("Result", C)

old = [1, [1, 2, 3], 3]
new = []
for i in old:
    new.append(i)
old = []
print("old", old)
print(new)
