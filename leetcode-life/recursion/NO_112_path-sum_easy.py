from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计：

子问题：每个到达叶子的路径的和，进行判断，是否是targetsum；
前进过程中增加和
"""

"""
初始递归：
找到所有的路径和
"""


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    sums = []

    def calSum(root: TreeNode, sum=0):
        if root:
            sum += root.val
            if not root.left and not root.right:
                sums.append(sum)
            calSum(root.left, sum)
            calSum(root.right, sum)

    calSum(root)
    # print(sums)
    if targetSum in sums:
        return True
    return False


"""
优化方法1：
只找到一个路径就可以
不停的减，根节点的时候，只要减的值和需要的结果相同就可以
所有的路径中，只一个返回true就可以
"""


def hasPathSum1(root: Optional[TreeNode], targetSum: int) -> bool:
    # 最外界的特例
    if not root:
        return False
    # 真正的边界
    if not root.right and not root.left:
        return targetSum == root.val
    return hasPathSum1(root.left, targetSum - root.val) or hasPathSum1(root.right, targetSum - root.val)


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node0.left = node1
node0.right = node2
node1.left = node3

print(hasPathSum1(node0, 4))
