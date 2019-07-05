#include<string>
#include<map>
using namespace std;
// 罗马数字转整数
class Solution {
public:
    int romanToInt(string s) {
        // map<char,int> morse = {
        //     {'I', 1},
        //     {'V', 5},
        //     {'X', 10},
        //     {'L', 50},
        //     {'C', 100},
        //     {'D', 500},
        //     {'M', 1000}
        // };
        map<char,int> strMap;
        strMap.insert(std::pair<char,int>('I', 1));
        strMap.insert(std::pair<char,int>('V', 5));
        strMap.insert(std::pair<char,int>('X', 10));
        strMap.insert(std::pair<char,int>('L', 50));
        strMap.insert(std::pair<char,int>('C', 100));
        strMap.insert(std::pair<char,int>('D', 500));
        strMap.insert(std::pair<char,int>('M', 1000));
        strMap.insert(std::pair<char,int>('A', -1));
        s = s + 'A';
        int result = 0;
        for(int i = 0; i<s.size()-1; i++) {
            if (strMap[s[i]] < strMap[s[i+1]])
                result -= strMap[s[i]];
            else
                result += strMap[s[i]];
        }
        return result;
    }
};