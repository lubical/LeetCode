#include <iostream>
using namespace std;
// 合并两个有序链表
struct ListNode {
     int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *p = new ListNode(0);
        ListNode *ans = p;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                p->next = l1;
                p = p->next;
                l1 = l1->next;
            } else {
                p->next = l2;
                p = p->next;
                l2 = l2->next;
            }
        }
        
        if (l1 != NULL) p->next = l1;
        if (l2 != NULL) p->next = l2;
        return ans->next;
    }
};