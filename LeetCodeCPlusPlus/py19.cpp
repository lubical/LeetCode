#include <iostream>
using namespace std;
// 一趟删除链表的倒数第N个节点，双指针，保持n的距离，到达底部，另一个即为所求。
struct ListNode {
     int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* preHead = new ListNode(0);
        preHead->next = head;
        ListNode *first, *second;
        first = preHead;
        second = preHead;
        for (int i=0;i<n+1;i++) {
            first = first->next;
        }
        while(first!=NULL) {
            first = first->next;
            second = second->next;
        }
        second->next = second->next->next;
        return preHead->next;
    }
};