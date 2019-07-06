#include <vector>
#include <string>
using namespace std;
class Solution {
    // 类似于BFS，每次在生成的所有串中依次添加该字符所对应的所有字符, 代码出自见底部
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        string charmap[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        if (digits=="")
            return res;
        res.push_back("");
        for (int i = 0; i < digits.size(); i++)
        {
            vector<string> tempres;
            string chars = charmap[digits[i] - '0'];
            for (int c = 0; c < chars.size();c++)
                for (int j = 0; j < res.size();j++)
                    tempres.push_back(res[j]+chars[c]);
            res = tempres;
        }
        return res;

// 作者：powcai
// 链接：https://leetcode-cn.com/problems/two-sum/solution/di-gui-he-fei-di-gui-by-powcai/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    }
};