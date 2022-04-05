# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计(不能思维定式)：

返回设计：
关键的边界设计：只有左右叶子节点都为空时，才返回1;左右子树中只一个为空时，为空的最小值不计算
"""


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    # 左右孩子都为空
    if not root.left and not root.right:
        return 1
    height = 10 ** 9
    # 左右孩子都不为空，选择最小的
    # 右孩子不为空
    if root.right:
        height = min(minDepth(root.right) + 1, height)
    # 左孩子不为空
    if root.left:
        height = min(minDepth(root.left) + 1, height)
    return height


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node0.left = node1
node0.right = node2
node1.left = node3

print(minDepth(node0))
