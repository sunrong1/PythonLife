from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计：
分解成子问题：每次生成，都又可能四左右生成，每次必须生成2个;生成过程中，结果不断累加；
全部n减少到1完成；
"""


def allPossibleFBT(n: int) -> List[TreeNode]:
    if n % 2 != 1:
        return list()
    result = []

    def fbt(num, tmp: List):
        if num == n:
            result.append(tmp)
            return
        t1 = 2
        t2 = TreeNode(0)
        tmp.left = t1
        tmp.right = t2
        fbt(num - 2, t1)
        if num - 2 != 0:
            fbt(num - 2, t2)

    tmp = [-1 for i in range(2 * n)]
    fbt(0, tmp)
    return result


r = allPossibleFBT(5)
print("树的个数：", len(r))

for i in r:
    print(i)
