#include <iostream>
using namespace std;
// 删除排序链表中的重复项，只保留一个
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
 };
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p = head;
        while (p!=NULL && p->next != NULL) {
            if (p->val == p->next->val) {
                ListNode *q = p->next;
                p->next = q->next;
                delete q;
                continue;
            }
            p = p->next;
        }  
        return head;
    }
};