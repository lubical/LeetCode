#include<string>
#include<vector>
using namespace std;
// 整数转罗马数字，按从到小，依次转换，拼接
class Solution {
public:
    string intToRoman(int num) {
        vector<int> value = { 1000,900,500,400,100,90,50,40,10,9,5,4,1};
		vector<string> dic = { "M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I" };
        string result = "";
        int index = 0;
        while (num>0 && index<value.size()) {
            if (num>=value[index]) {
                result += dic[index];
                num -= value[index];
            }else
                index++;
        }
        // for(int i=0;i<value.size();i++) {
        //      if (num/value[i] == 0)
        //          continue;
        //      for (int j=0;j<num/value[i];j++)
        //          result += dic[i];
        //      num -= num/value[i]*value[i];
        // }
        return result;
    }
};