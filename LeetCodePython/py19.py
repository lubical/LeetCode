# 一趟删除链表的倒数第N个节点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        preHead  = ListNode(0)
        preHead.next = head
        first = preHead
        second = preHead
        for i in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return preHead.next
        
        
        
        