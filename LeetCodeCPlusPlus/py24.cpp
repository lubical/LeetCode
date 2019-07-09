#include <iostream>
using namespace std;
// 两两交换链表节点
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode * result = new ListNode(0);
        ListNode *pre = result, *p, *q;
        result->next = head;
        p = head;
        while (p!=NULL && p->next!=NULL) { // 还有连续的两个
            q = p->next;       // 取下一个
            p->next = q->next; // 接下后续的
            q->next = p;       // 交换完成
            pre->next = q;     // 接上之前的
            pre = p;           // 前指针后移
            p = p->next;       // 当前指针后移
        }
        pre->next = p;     // 接上可能剩下的单个节点
        return result->next;
    }
};