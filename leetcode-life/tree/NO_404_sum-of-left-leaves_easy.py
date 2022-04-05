from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归设计：

左叶子的判断：
"""


# 错误示例，sum 输出为0
def sumOfLeftLeaves_error(root: Optional[TreeNode]) -> int:
    sum = 0

    def sumLeaves(root: TreeNode):
        if not root:
            return
        if not root.left and not root.right:
            global sum
            sum = sum + root.val
            print(sum)
        sumLeaves(root.left)
        sumLeaves(root.right)

    sumLeaves(root)
    return sum


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    def sumLeaves(root: TreeNode):
        sum = 0
        if root.left:
            # 左节点存在，且是叶子节点
            if not root.left.left and not root.left.right:
                sum = sum + root.left.val
            else:
                sum = sum + sumLeaves(root.left)
        if root.right:
            if root.right.left or root.right.right:
                sum = sum + sumLeaves(root.right)
        return sum

    return sumLeaves(root)


node0 = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(17)
node0.left = node1
node0.right = node2

node2.left = node3
node2.right = node4

print("sum", sumOfLeftLeaves(node0))
num = 1  # 这是一个全局变量 为了美观我把他放在第一行


def update():  # 示例函数
    global num  # 使用global声明num，在函数中就可以修改全局变量的值
    num += 1  # 全局变量可以参与运算
    return 0

#
# print(num)  # 调用函数前查看全局变量
# update()  # 调用函数，修改全局变量
# print(num)  # 调用函数后查看全局变量
