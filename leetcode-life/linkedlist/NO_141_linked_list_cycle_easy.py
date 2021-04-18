
# import myLinkedList
class ListNode:
    def __init__(self,x):
        self.val =x
        self.next = None
# 链表中环的判断
# 方法1，快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow and slow == fast:
                return True
        return False
