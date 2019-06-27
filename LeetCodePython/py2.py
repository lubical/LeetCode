class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mySum(self, x, y):
        return (x+y)%10, (x+y)//10
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        
        if not l1:
            return l2
        elif not l2:
            return l1
        
        result = ListNode(0)
        pre = result
        plus = 0
        while(l1 and l2):
            total, plus = self.mySum(l1.val+plus, l2.val) 
            q = ListNode(total)
            pre.next = q
            pre = q
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total,plus = self.mySum(l1.val, plus)
            q = ListNode(total)
            pre.next = q
            pre = q
            l1 = l1.next
        
        while l2:
            total,plus = self.mySum(l2.val, plus)
            q = ListNode(total)
            pre.next = q
            pre = q
            l2 = l2.next
        
        if plus:
            q = ListNode(plus)
            pre.next = q
            pre = q
            
        pre.next = None
            
        return result.next

def construct(data:list):
    head = ListNode(0)
    pre = head
    for item in data:
        temp = ListNode(item)
        pre.next = temp
        pre = temp
    return head.next

if __name__ == '__main__':
    import time
    start = time.process_time()
    a = [2,4,3]
    b = [5,6,4]
    l1 = construct(a)
    l2 = construct(b)
    ans = Solution().addTwoNumbers(l1, l2)
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
    end = time.process_time()
    print("run time:",str(end-start))
