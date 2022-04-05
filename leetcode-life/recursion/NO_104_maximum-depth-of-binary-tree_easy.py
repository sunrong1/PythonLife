from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
方法1：递归解决
子问题：左右子树的最大深度
前进段：不做啥，到边界返回
后退段：获取每个root点的最大高度，root 为空，高度为1
边界：root为空
"""


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    height = max(leftHeight, rightHeight) + 1
    return height


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node0.left = node1
node0.right = node2
print(maxDepth(node0))
