# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
关键规律：
循环+ 非循环  /循环 + 非循环/... 

双指针法
l 是最后一个不重复元素的开头
r 忘后走，走到没有重复的元素为止：
重复判断

h 1 1 2 3 3 4 4 5
l r
l   r       # 循环进行 r.val == r.next.val --> r= r.next 


h 1 1 1 2 3 3 4 4 5
l r 
l      
"""


def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return head
    h = ListNode(-1)
    l = h
    r = head
    while r:
        # 跳出第一个循环
        if r.next:
            dValue = r.next.val
            while r.next and r.val == r.next.val:
                r = r.next
            if r.val == dValue:
                r = r.next
        if not r:
            break
        # 当前值有效加到不重复链表中
        if r.next is None or r.val != r.next.val:
            # 注意赋值的先后顺序,赋值后再变化
            l.next = r
            r = r.next
            l = l.next
            # l.next 要清空，否者就继承了上个r的
            l.next = None
    return h.next


head0 = ListNode(1)
head1 = ListNode(2)
head2 = ListNode(3)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(4)
head6 = ListNode(5)
head0.next = head1
head1.next = head2
head2.next = head3
head3.next = head4
head4.next = head5
head5.next = head6

h0 = ListNode(1)
h1 = ListNode(2)
h2 = ListNode(2)
h0.next = h1
h1.next = h2
print(deleteDuplicates(head0))
