"""
节点的填充
层序遍历，广度优先遍历
# Definition for a Node.
1more
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
方法1
层序遍历,每一层的节点从左向后关联即可。注意顺序
关键的是，使用队列存储数据
"""


def connect(root: Node) -> Node:
    if not root:
        return None
    q = []
    q.append(root)
    while q:
        num = len(q)
        pre = None
        for i in range(num):
            node = q.pop()
            if pre:
                pre.next = node
            pre = node
            if node.left:
                q.insert(0, node.left)
            if node.right:
                q.insert(0, node.right)
    return root


def levelOrder(root: Node):
    if not root:
        return None
    ret = []
    ret.append(root)
    while ret:
        node = ret.pop()
        print(node.val)
        if node.left:
            ret.append(node.left)
        if node.right:
            ret.append(node.right)


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node0.left = node1
node0.right = node2
node1.left = node3
levelOrder(node0)
