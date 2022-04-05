"""
平衡二叉树的判断
每个节点的两个子树的高度差是1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计：

子问题：判断左右子树的高度。高度的计算，左右子树高度+1
前进段：判断每个左右子树的高度差，
后退段：
边界分析：遇到叶子节点返回；高度差>1 返回false。否者遍历结束，高度>1 就是true
"""


def isBalanced(root: TreeNode) -> bool:
    def maxHeight(root):
        if not root:
            return 0
        leftHeight = maxHeight(root.left)
        rightHeight = maxHeight(root.right)
        if leftHeight == -1 or leftHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        height = max(leftHeight, rightHeight) + 1
        return height

    return maxHeight(root) >= 0


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node0.left = node1
node0.right = node2
node1.left = node3
node3.left = node4
print(isBalanced(node0))
