// 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
// 你应当保留两个分区中每个节点的初始相对位置。


#include <iostream>
using namespace std;
 struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *dummy1 = new ListNode(0);
        ListNode *dummy2 = new ListNode(0);
        ListNode *p = dummy1, *q = dummy2;
        while (head!=NULL) {
            if (head->val < x) {
                p->next = head;
                p = p->next;
            } else {
                q ->next = head;
                q = q->next;
            }
            head = head->next;
        }
        p->next = dummy2->next;
        q->next = NULL;
        return dummy1->next;
    }
};