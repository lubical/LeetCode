#include<string>
#include <regex>
using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        string re = "^\\s*([\\+-]?)0*(\\d+)(.*)";  //c++ regex_match是整段匹配的，(.*)不能少，否则匹配失败。去掉前导0
        regex rule(re);
        std::smatch sm;
        bool ret = regex_match(str, sm, rule);
        if (not ret)
            return 0;
    
        string min_str = to_string(INT_MIN);
        string max_str = to_string(INT_MAX);
    
        string s = sm[1]!='+'? string(sm[1])+string(sm[2]): string(sm[2]); //拼接符号与非0前缀的数字,正数不需要符号


        if (s[0]=='-'){
             if (s.size() > min_str.size() || s.size() == min_str.size()&& s > min_str)
                 return INT_MIN;
        }else if (s.size() > max_str.size() || s.size() == max_str.size()&& s > max_str)
            return INT_MAX;
        
        return atoi(s.c_str());

    }
};