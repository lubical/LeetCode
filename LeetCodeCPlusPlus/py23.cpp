
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
// 合并K个有序链表，优先队列实现
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int,int> > > queue; // 注意>>代表右移，所以空格不能少
        // greater对应小顶堆、less默认对应大顶堆
        for (int i=0;i<lists.size();i++)
            if (lists[i]!=NULL) {
                queue.push(pair<int,int>(lists[i]->val, i));
                lists[i] = lists[i]->next;
            }
        ListNode* result = new ListNode(0);
        ListNode* p = result;
        while(!queue.empty()) {
            pair<int,int>tmp = queue.top();  // 获取队头
            p->next = new ListNode(tmp.first);
            p = p->next;
            queue.pop();  // 弹出
            if (lists[tmp.second]!=NULL) {
                queue.push(pair<int,int>(lists[tmp.second]->val, tmp.second)); // 不空，继续加入队
                lists[tmp.second] = lists[tmp.second]->next;
            }
        }
        return result->next;      
        
    }
};