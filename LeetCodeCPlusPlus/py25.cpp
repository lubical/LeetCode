#include <iostream>
using namespace std;
// K个一组，翻转链表，不足K个无需翻转。尾插法。不足K个进行两次尾插法还原
 struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode(0);
        ListNode *tail = head,*tmp; // head交换后到末尾
        int i = 0;
        while (head!=NULL && i<k) {
            tmp = head->next;
            head->next = dummy->next;
            dummy->next = head;
            head = tmp;
            i++;
        }
        if (head!=NULL) 
            tail->next = reverseKGroup(head, k);
        else if (i<k) { // 不足k个，再逆序回来
            head = dummy->next;
            dummy->next = NULL;
            while (head!=NULL) {
                tmp = head->next; // 保留下一个
                head->next = dummy->next;  // 往前插入保留后续
                dummy->next = head;  // 往前插入
                head = tmp; // 后移
            }
        }
        return dummy->next;
    }
};