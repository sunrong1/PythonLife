from myLinkedList import *


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        链表反转
        
        :param head:
        :return:
        """
        if not head or head.next is None:
            return head
        pos_left = ListNode(-1)
        pos_left.next = head

        pos = 0
        while pos < left - 1:
            pos_left = pos_left.next
            pos += 1
        pos_right = pos_left
        while pos < right:
            pos_right = pos_right.next
            pos += 1
        num = right - left + 1
        while num > 0:
            tmp = pos_left.next
            pos_left


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
s = Solution()
c = s.reverseList(a)
c.node_print()
