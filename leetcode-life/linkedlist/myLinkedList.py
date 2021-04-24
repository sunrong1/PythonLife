class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def node_print(self):
        while self:
            print(self.val)
            self = self.next
