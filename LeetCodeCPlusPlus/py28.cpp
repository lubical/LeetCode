#include <string>
using namespace std;
// 实现 strStr() 函数。
// 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle == "")
            return 0;
        if (haystack.size()<needle.size())
            return -1;
        for (int i=0;i<=haystack.size()-needle.size();i++) {
            bool find = true;
            for (int j=0;j<needle.size();j++) 
                if (haystack[i+j]!=needle[j]) {
                    find = false;
                    break;
                }
            if (find)
                return i;
        }
        
        return -1;
        
    }
};