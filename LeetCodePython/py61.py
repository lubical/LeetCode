# 旋转链表 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        p = head
        n = 0
        while p:  # 算长度
            n += 1
            p = p.next
        
        k = k % n  # 需要移动的位置
        if k == 0: # 不需要移动，直接返回原来的
            return head
        p = head
        while k>0 and p:  # 先移动一个指针
            p = p.next
            k -= 1
        q = head
        while p.next:   # 同时移动两个指针，保持距离为k
            q = q.next
            p = p.next
        
        result = q.next # 新的头结点
        p.next = head  # 接上原来的head所指向的节点
        q.next = None  # 新的尾结点
        return result