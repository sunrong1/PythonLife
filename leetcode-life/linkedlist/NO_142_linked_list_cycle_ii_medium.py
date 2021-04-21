from myLinkedList import *


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        一道典型的数学证明题
        将距离划分为a b c 断，a+b 获得相遇的点，证明a = c
        判断链表中环的位置
        :param head:
        :return:
        """
        if not head:
            return None
        start, slow, fast = head, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow and slow == fast:
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start
        return None
