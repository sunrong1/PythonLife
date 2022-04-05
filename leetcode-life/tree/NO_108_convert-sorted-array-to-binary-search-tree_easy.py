from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计：
关键子问题：每次取中间位置的点作为root点，然后前进创建左右子树
边界条件：数字条件不满足

"""


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def sort(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(mid)
        node.left = sort(left, mid - 1)
        node.right = sort(mid + 1, right)
        return node

    return sort(0, len(nums) - 1)
