#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    // 最长公共前缀
    string longestCommonPrefix(vector<string>& strs) {
        string result = "";
        int index = 0;
        while (strs.size()>0) {
            char c = strs.size()>0 and strs[0].size()>index? strs[0][index]:' ';
            for(int i = 0;i<strs.size();i++) 
                if (strs[i].size() < index || strs[i][index]!= c)
                    return result;
            index++;
            result += c;
        }
        return result;
    }
};