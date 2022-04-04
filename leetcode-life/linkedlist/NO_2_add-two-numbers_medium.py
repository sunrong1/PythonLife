from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = None
    add_forehead = 0
    pre_node = None
    while l1 or l2:
        sum = 0
        if l1 is None or l2 is None:
            if l1 is None:
                sum = l2.val + add_forehead
                l2 = l2.next
            else:
                sum = l1.val + add_forehead
                l1 = l1.next
        else:
            sum = l1.val + l2.val + add_forehead
            l1 = l1.next
            l2 = l2.next
        if sum >= 10:
            # 可优化，合并成1句
            add_forehead = sum // 10
            sum = sum % 10
        else:
            add_forehead = 0
        temp = ListNode(sum, None)
        if result is None:
            result = temp
            pre_node = temp
        else:
            pre_node.next = temp
            pre_node = temp

    if add_forehead == 1:
        temp = ListNode(1, None)
        pre_node.next = temp
    return result


# 有默认参数，可以不加none
node0 = ListNode(2, None)
node1 = ListNode(4, None)
node2 = ListNode(3, None)
node0.next = node1
node1.next = node2

node3 = ListNode(5, None)
node4 = ListNode(6, None)
node5 = ListNode(4, None)
node3.next = node4
node4.next = node5

node = addTwoNumbers(node0, node3)
while node:
    print(node.val)
    node = node.next
