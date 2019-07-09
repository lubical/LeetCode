# 两两交换链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode(0)
        result.next = head
        pre = result
        p = head
        while p and p.next:
            q = p.next        # 取下一个
            p.next = q.next   # 保留后一个
            q.next = p        # 交换
            pre.next = q  # 接上前面的
            pre = p       # 新的前一个位置
            p = p.next    # 移动当前位置
        pre.next = p   # 接上最后剩下的单个节点
        return result.next