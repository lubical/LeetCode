// 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
// 2019.7.29
#include <iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int length = 0;
        ListNode *p = head;
        if (head == NULL)
            return head;
        while (p->next != NULL) { // 找到末尾
            length++;
            p = p->next;
        }
        p->next = head; // 先拼接成链
        k %= ++length;
        p = head;
        for (int i=0;i<length-k-1;i++) { // 再找断开位置
            p = p->next;
        }
        head = p->next; // 新的头结点
        p->next = NULL;  // 断开
        return head;
    }
};