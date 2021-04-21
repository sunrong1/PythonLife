from myLinkedList import *


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        方法1，快慢指针
        链表中环的判断
        :param head:
        :return:
        """
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow and slow == fast:
                return True
        return False
