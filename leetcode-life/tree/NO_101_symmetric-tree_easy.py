from typing import Optional

"""
树的对称性

对称的特点
1. 递归实现；

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def dfs(left, right):
        if left is None and right is None:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        isSame = dfs(left.left, right.right)
        isSame = isSame and dfs(left.right, right.left)
        return isSame

    return dfs(root.left, root.right)


node1 = TreeNode(1, None, None)
node2 = TreeNode(2, None, None)
root = TreeNode(0, node1, node2)
print(isSymmetric(root))
