from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计：
子问题：每个叶子节点返回，保存一次路径；否者就一直增加
前进段：主要再前进段不停的增加str结果
边界问题：判断是否是叶子节点

数据结构设计
“1->” 一个子问题

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]


"""


def binaryTreePaths(root: TreeNode) -> List[str]:
    paths = []

    def buildPath(root: TreeNode, path):
        if root:
            path += str(root.val)
            # 叶子节点
            if not root.left and not root.right:
                paths.append(path)
            # 否者肯定有一个非空
            else:
                path += '->'
                buildPath(root.left, path)
                buildPath(root.right, path)

    buildPath(root, '')
    return paths


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node0.left = node1
node0.right = node2
node1.left = node3

print(binaryTreePaths(node0))
