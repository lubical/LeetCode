# Definition for singly-linked list.
# K个一组翻转，不足K个无需翻转
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 尾插法，不足K个时，再进行一次尾插法
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        i = 0
        dummy = ListNode(0)
        tail = head  # 第一个节点交换后成为最后一个节点
        while i<k and head:  
            tmp = head.next  # 插入到头部，即逆序
            head.next = dummy.next
            dummy.next = head
            head = tmp
            i += 1
        if head:
            tail.next = self.reverseKGroup(head, k)
        elif i<k: # head为空时，应该判断是否个数不足
            head = dummy.next
            dummy.next = None # 重新断掉
            while head:
                tmp = head.next
                head.next = dummy.next
                dummy.next = head
                head = tmp 
        
        return dummy.next

class Solution2:
    # 栈实现，懒得写了。
    ## 作者：powcai
    ##  链接：https://leetcode-cn.com/problems/two-sum/solution/kge-yi-zu-fan-zhuan-lian-biao-by-powcai/
    ##  来源：力扣（LeetCode）
    ##  著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k 
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count : 
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            #与剩下链表连接起来 
            p.next = tmp
            head = tmp


        
            
        