from myLinkedList import *

class Solution:
    def isHappy(self, n: int) -> bool:
        """

        :param n:
        :return:
        """
        if not head:
            return None
        start,slow,fast= head,head,head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            if slow and slow == fast:
                while start != slow:
                    start = start.next
                    slow =slow.next
                return start
        return None


