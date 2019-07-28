// 最后一个单词的长度
#include <string>
using namespace std;
class Solution {
public:
    int lengthOfLastWord(string s) {
        int end = s.size() - 1;
        while (end>=0 && s[end] == ' ')
            end--;
        int start = end;
        while (start>=0 && s[start] != ' ')
            start--;
        return end-start; 
    }
};