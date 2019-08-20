#include <iostream>
using namespace std;
// 删除链表中含有重复值的项；快慢指针
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *slow = dummy, *fast = dummy->next;
        while (fast!=NULL) {
            if (fast->next != NULL && fast->next->val == fast->val) {
                int temp = fast->val;
                while (fast !=NULL && fast->val == temp)
                    fast = fast->next;
            }else {
                slow->next = fast;
                slow = slow->next;
                fast = fast->next;
            }
        }
        slow->next = fast;
        return dummy->next;
    }
};