from myLinkedList import *


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        方法1：头插法，记得绘图，记得节点值的更新点和更新顺序，可以先列出来需要更新的节点next值
        next值，即是连接关系
        链表反转
        
        :param head:
        :return:
        """
        if not head or head.next is None:
            return head
        # 技巧1：涉及对头节点的变更，增加Dump的头节点
        dummy = ListNode(-1)
        dummy.next = head
        # 定义pre的位置编号,并且先走到left-1的位置
        pre = dummy
        pos = 0
        while pos < left - 1:
            pre = pre.next
            pos += 1
        # left_p 保持位置不变，不断从下一位插入后面元素，实现反转
        curr = pre.next
        while pos < right - 1:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
            pos += 1

        return dummy.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
s = Solution()
c = s.reverseBetween(a, 1, 2)
c.node_print()
