from typing import List 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 合并K个有序链表
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 来源于LeetCode-cn用户powcai, 堆排序优化
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):  # 将每一个链第一个节点放入堆中
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)  # 弹出，新建
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:  # 不为空 
                heapq.heappush(head, (lists[idx].val, idx))  # 放入下一个 
                lists[idx] = lists[idx].next
        return dummy.next

class Solution2:
    # 分治
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            result = ListNode(0)
            p = result
            first = lists[0]
            second = lists[1]
            while first and second:
                if first.val<=second.val:
                    p.next = first
                    p = p.next
                    first = first.next
                else:
                    p.next = second
                    p = p.next
                    second = second.next
            if first:
                p.next = first
            if second:
                p.next = second
            return result.next
        else:
            left = self.mergeKLists(lists[:len(lists)//2])  
            right = self.mergeKLists(lists[len(lists)//2:])  
            return self.mergeKLists([left,right])     



        
        