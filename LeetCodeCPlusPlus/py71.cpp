// 简化路径 linux路径 
#include<sstream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    string simplifyPath(string &path) {
        for(int i=path.length(); i--; path[i]=(path[i]=='/'?' ':path[i])); // 将/替换成空格，以分隔字符
        stringstream istr(path);  // 以空格分隔的字符流
        
        vector<string> vs;
        string str;
        while(istr>>str){
            if(str==".") continue;
            if(str!="..") vs.push_back(str);
            else if(vs.size()) vs.pop_back();
        }
        str.clear();
        for(int i=0; i<vs.size(); str.append("/"+vs[i++]));
        return str.length()?str:"/";
    }
};