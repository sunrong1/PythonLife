"""
另一棵树的子树

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
方法1：
相等条件：递归判断，根节点 左孩子节点 右孩子节点相等，否者不相等
"""


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root:
        return False

    def isSame(tree: TreeNode, subTree: TreeNode):
        if not tree and not subTree:
            return True
        if not tree or not subTree:
            return False
        if tree.val != subTree.val:
            return False
        return isSame(tree.left, subTree.left) and isSame(tree.right, subTree.right)

    def dfs(tree1: TreeNode, tree2: TreeNode):
        if not tree1:
            return False
        return isSame(tree1, tree2) or dfs(tree1.left, tree2) or dfs(tree1.right, tree2)

    return dfs(root, subRoot)


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node0.left = node1
node0.right = node2
node1.left = node3

node11 = TreeNode(1)
node33 = TreeNode(3)
node11.left = node33
print(isSubtree(node0, node11))
