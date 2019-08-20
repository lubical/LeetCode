// 最小覆盖子串；滑动窗口
#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    string minWindow(string s, string t) {
    // 记录最短子串的开始位置和长度 滑动窗口，先找到满足的最小长度，在缩减左区间直到不满足，之后找下一个满足的长度。
    int start = 0, minLen = INT_MAX;
    int left = 0, right = 0;
    
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for (char c : t) needs[c]++; // 不存在的键会自动赋值为0
    
    int match = 0;
    
    while (right < s.size()) {
        char c1 = s[right];
        if (needs.count(c1)) {
            window[c1]++;
            if (window[c1] == needs[c1]) 
                match++;
        }
        right++;
        
        while (match == needs.size()) {
            if (right - left < minLen) {
                // 更新最小子串的位置和长度
                start = left;
                minLen = right - left;
            }
            char c2 = s[left];
            if (needs.count(c2)) {
                window[c2]--;
                if (window[c2] < needs[c2])
                    match--;
            }
            left++;
        }
    }
    return minLen == INT_MAX ?
                "" : s.substr(start, minLen);
}

// 作者：labuladong
// 链接：https://leetcode-cn.com/problems/two-sum/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
};