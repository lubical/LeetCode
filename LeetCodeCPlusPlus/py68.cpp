// 文本左右对齐
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        int begin = 0, width = 0;
        for (int i = 0; i < words.size(); i++) {
            // width 是所有字符的总长度， i - begin是需要加的空格
            if (width + words[i].size() + i - begin > maxWidth) {
                ans.push_back("");  // 先插入空字符，后续计算
                if (i - begin <= 1) {
                    ans.back() += words[begin];
                    ans.back() += string(maxWidth - ans.back().size(), ' ');
                } else {
                    int quo = (maxWidth - width) / (i - begin - 1);  // 不包括i，空格数为i-begin-1
                    int rem = (maxWidth - width) % (i - begin - 1);
                    for (int j = begin; j < i - 1; j++) {
                        ans.back() += words[j];
                        ans.back() += string(j < begin + rem ? quo + 1 : quo, ' ');
                    }
                    ans.back() += words[i - 1];
                }
                begin = i;
                width = 0;
            }
            width += words[i].size();
        }
        ans.push_back("");
        for (int i = begin; i < words.size() - 1; i++) {
            ans.back() += words[i];
            ans.back() += ' ';
        }
        ans.back() += words.back();
        ans.back() += string(maxWidth - ans.back().size(), ' ');
        return ans;
    }
};

/*
作者：gremist
链接：https://leetcode-cn.com/problems/two-sum/solution/c-fen-lei-tao-lun-ti-jie-by-gremist/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/