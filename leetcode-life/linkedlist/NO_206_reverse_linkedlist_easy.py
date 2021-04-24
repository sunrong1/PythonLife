from myLinkedList import *


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        """
        方法1：迭代法，搞清循环挂载顺序就可以
        链表反转
        :param head:
        :return:
        """
        if not head:
            return head
        result = None
        tmp = head
        while tmp:
            tmp2 = tmp.next
            tmp.next = result
            result = tmp
            tmp = tmp2
        return result


a = ListNode(1)
b = ListNode(2)
a.next = b
s = Solution()
c = s.reverseList(a)
c.node_print()
