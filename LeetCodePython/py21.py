# 合并两个有序链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        p = ans
        while (l1 and l2):
            if l1.val <= l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return ans.next
        