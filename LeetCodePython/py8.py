# 字符串转换为整数
class Solution:
    # 解法一：一个个拆分
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        str = str.strip() # 去空格
        if not str:
            return 0
        print(str)
        index = 0
        
        flag = -1 if str[index] == '-' else 1
        if str[index] in ['+','-']:
            index += 1
        try:
            ans = 0
            while index<len(str) and str[index].isdigit():
                if flag == 1 and (ans > INT_MAX//10 or ans==INT_MAX//10 and int(str[index])>7):
                    return INT_MAX
                if flag == -1 and (ans > INT_MIN//-10 or ans ==INT_MIN//-10 and int(str[index])>8):
                    return INT_MIN
                ans = ans*10 + int(str[index])
                index += 1
            return ans*flag
        except:
            return 0

# import re
# class Solution:
#     # 解法二 正则表达式
#     def myAtoi(self, str: str) -> int:
#         matchObj = re.match( r'\s*([\+|-]?\d+)', str)
#         if not matchObj:
#             return 0
#         else:
#             ans = int(matchObj.group(1))
#             MIN_INT = -2**31
#             MAX_INT = 2**31-1
#             if ans<MIN_INT:
#                 return MIN_INT
#             elif ans>MAX_INT:
#                 return MAX_INT
#             else:
#                 return int(ans)
        
            
        