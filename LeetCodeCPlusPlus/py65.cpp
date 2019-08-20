//验证给定的字符串是否可以解释为十进制数字。
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isNumber(string &s) {
        vector<unordered_map<string, int>> state{
            {{}}, 
            {{"blank",1}, {"sign",2}, {"digit",3}, {"dot",4}},  // 状态一
            {{"digit",3}, {"dot",4}}, // 状态二
            {{"digit",3}, {"dot",5}, {"e",6}, {"blank",9}},  // 状态三
            {{"digit",5}}, // 状态四
            {{"digit",5}, {"e",6}, {"blank",9}}, // 状态五
            {{"sign",7}, {"digit",8}}, //状态六
            {{"digit",8}}, // 状态七
            {{"digit",8}, {"blank",9}}, // 状态八
            {{"blank",9}}
        };
        
        int cur_state = 1;
        string type = "";
        for (auto ch: s) {
            type = ch;
            if (ch>='0' && ch<='9') 
                type = "digit";
            else if (ch == ' ')
                type = "blank";
            else if (ch == '.')
                type = "dot";
            else if (ch == '+' || ch == '-')
                type = "sign";
            if (state[cur_state].count(type) == 0)
                return false;
            cur_state = state[cur_state][type];
            
        }
        return (cur_state == 3 || cur_state == 5 || cur_state == 8 || cur_state == 9);
    }
};

class Solution2 {
public:
    bool isNumber(string &s) {
        // regex r("\\s*[+-]?(\\d+\\.?\\d*|\\.\\d+)(e[+-]?\\d+)?\\s*$");
        int i=s.find_first_not_of(' ');
        int d1=0, dot=0, d2=0, e=0, d3=0;
        if(s[i]=='+' || s[i]=='-') ++i;
        for(; i<s.length() && isdigit(s[i]); d1=++i);
        if(i<s.length() && s[i]=='.') dot=++i;
        for(; i<s.length() && isdigit(s[i]); d2=++i);
        if(dot && !d1 && !d2) return false;
        if(i<s.length() && (d1||d2) && s[i]=='e') e=++i;
        if(i<s.length() && e && (s[i]=='+'|s[i]=='-')) ++i;
        for(; i<s.length() && isdigit(s[i]); d3=++i);
        if(e && (!(d1||d2) || !d3)) return false;
        for(; i<s.length() && s[i]==' '; ++i);
        return i==s.length();
    }
};

// 作者：joy-teng
// 链接：https://leetcode-cn.com/problems/two-sum/solution/shou-dong-pan-ding-te-ding-zheng-ze-biao-da-shi-by/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。