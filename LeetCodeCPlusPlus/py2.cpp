#include<iostream>
#include<vector>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* temp = head;
        int carry = 0;
        while(l1 != NULL || l2 != NULL) {
            int oper1 = (l1 == NULL) ? 0 : l1->val;
            int oper2 = (l2 == NULL) ? 0 : l2->val;
            int operSum = oper1 + oper2 + carry;
            carry = operSum / 10;
            int add = operSum % 10;
            temp->next = new ListNode(add);
            temp = temp->next;
            if(l1 != NULL) l1 = l1->next;
            if(l2 != NULL) l2 = l2->next;
        }
        if(carry>0) {
            temp->next = new ListNode(carry);
        }
        return head->next;
    }

    ListNode* construct(vector<int> a) {
        ListNode* head = new ListNode(0);
        ListNode* temp = head;
        for (int i=0;i<a.size();i++) {
            temp->next = new ListNode(a[i]);
            temp = temp->next;
        }
        return head->next;
    }
};

int main(){
    Solution solution = Solution();
    vector<int> a = {2, 7, 1, 5};
    vector<int> b = {3, 3, 2, 4};
    ListNode* l1 = solution.construct(a);
    ListNode* l2 = solution.construct(b);
    ListNode* ans = solution.addTwoNumbers(l1, l2);
    while (ans != NULL) {
        cout << ans->val << " ";
        ans = ans->next;
    }
    return 0;

}