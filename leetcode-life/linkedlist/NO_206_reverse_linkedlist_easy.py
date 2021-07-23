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
        curr = None  # 注意结束标识，否则会出现循环链表
        nx = head
        while nx:
            temp = nx.next
            nx.next = curr
            curr = nx
            nx = temp
        return curr


a = ListNode(1)
b = ListNode(2)
a.next = b
s = Solution()
c = s.reverseList(a)
c.node_print()
