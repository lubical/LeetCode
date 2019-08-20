# 删除链表中含有重复值的所有项
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        result = ListNode(0)
        q = result
        while p and p.next:
            same = False
            while p.next and p.val == p.next.val:
                same = True
                p.next = p.next.next
            if not same:
                q.next = p
                q = q.next
            p = p.next
       
        q.next = p if p else None
        return result.next