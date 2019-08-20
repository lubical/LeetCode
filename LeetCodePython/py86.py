# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

# 你应当保留两个分区中每个节点的初始相对位置。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        p = dummy1
        q = dummy2
        while head:  # 双链拆分再合并
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        p.next = dummy2.next
        q.next = None
        return dummy1.next

class Solution2: # 法二：类似冒泡排序，先链表逆序，往前插入，再逆序一次返回结果
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        p = head
        tail = None
        while p:  # 先逆序，同时插入
            q = p.next
            if p.val >= x or not tail or tail.val < x:
                p.next = tail
                tail = p
            else:
                look_p_pre = tail
                while look_p_pre.next and look_p_pre.next.val >= x:  # 查找插入的位置
                    look_p_pre = look_p_pre.next
                p.next = look_p_pre.next
                look_p_pre.next = p
 
            p = q
       
        
        p_pre = None
        p = tail
        while p.next:  # 再一次逆序回来
            q = p.next
            p.next = p_pre
            p_pre = p
            p = q
        p.next = p_pre
        
        return p