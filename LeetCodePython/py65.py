# 有效数字 十进制数
# 解法一：直接分情况，将字符串拆分为整数部分、小数部分和指数部分。
# 解法二：自动机
# 解法三：直接判断，dot，e，num，与一类似
# 解法四： 正则表达式 r("\\s*[+-]?(\\d+\\.?\\d*|\\.\\d+)(e[+-]?\\d+)?\\s*$");
class Solution:
    # 解法一：
    def isNumber(self, s: str) -> bool:
        nums = {'0','1','2','3','4','5','6','7','8','9'}
        plus_and_minus = {'+','-'}
        rank_and_dot = {'e','.'}
        def all_number(ss: str) -> bool:
            if not ss:
                return False
            for ch in ss:
                if ch not in nums:
                    return False
            return True
        
        def all_number_with_plusAndMinus(ss: str) -> bool:
            if not ss:
                return False
            if ss[0] in plus_and_minus:
                return all_number(ss[1:])
            else:
                return all_number(ss)
          
        
        rank_pos = -1
        dot_pos = -1
        s = s.strip()

        for pos, ch in enumerate(s):
            if ch not in nums|plus_and_minus|rank_and_dot: # 无效字符直接返回False
                return False
            
            if ch == 'e':  # 记录阶所在的位置
                rank_pos = pos
            elif ch == '.': # 记录小数点所在的位置，小数点前后只能有一处为空
                dot_pos = pos
     
        if dot_pos != -1 and rank_pos != -1 and dot_pos > rank_pos:  # 指数只能为整数
            return False
    
        if rank_pos == -1:  # 没有指数形式，只能是以符号数字开头
            if dot_pos == -1:  # 无小数 .1 True 1. True
                return s and all_number_with_plusAndMinus(s)
            else:
                if not s[:dot_pos] or s[:dot_pos] in plus_and_minus:  # 小数点前为空,或小数点前只有一个符号
                    return all_number(s[dot_pos+1:])
                if not s[dot_pos+1:]: #小数点后为空
                    return all_number_with_plusAndMinus(s[:dot_pos])
                
                #小数点前后均不为空
                return all_number_with_plusAndMinus(s[:dot_pos]) and all_number(s[dot_pos+1:])
        else:
            if dot_pos == -1: # 无小数
                return  all_number_with_plusAndMinus(s[:rank_pos]) and all_number_with_plusAndMinus(s[rank_pos+1:])
            else:  # 有小数
                
                if not s[:dot_pos] or s[:dot_pos] in plus_and_minus:  # 小数点前为空,或小数点前只有一个符号
                    return all_number(s[dot_pos+1:rank_pos]) and all_number_with_plusAndMinus(s[rank_pos+1:])
                if not s[dot_pos+1:rank_pos]: # 小数点后为空
                    return all_number_with_plusAndMinus(s[:dot_pos]) and all_number_with_plusAndMinus(s[rank_pos+1:])
                
                return  all_number_with_plusAndMinus(s[:dot_pos]) and all_number(s[dot_pos+1:rank_pos]) and \
                       all_number_with_plusAndMinus(s[rank_pos+1:])
       
        return False

class Solution2:
    # 解法二：自动机
    def isNumber(self, s: str) -> bool:
        state = [
            {},
            # 状态1,初始状态(扫描通过的空格)
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            # 状态2,发现符号位(后面跟数字或者小数点)
            {"digit": 3, ".": 4},
            # 状态3,数字(一直循环到非数字)
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            # 状态4,小数点(后面只有紧接数字)
            {"digit": 5},
            # 状态5,小数点之后(后面只能为数字,e,或者以空格结束)
            {"digit": 5, "e": 6, "blank": 9},
            # 状态6,发现e(后面只能符号位, 和数字)
            {"sign": 7, "digit": 8},
            # 状态7,e之后(只能为数字)
            {"digit": 8},
            # 状态8,e之后的数字后面(只能为数字或者以空格结束)
            {"digit": 8, "blank": 9},
            # 状态9, 终止状态 (如果发现非空,就失败)
            {"blank": 9}
        ]
        cur_state = 1
        for c in s:
            if c.isdigit():
                c = "digit"
            elif c in " ":
                c = "blank"
            elif c in "+-":
                c = "sign"
            if c not in state[cur_state]:
                return False
            cur_state = state[cur_state][c]
        if cur_state not in [3, 5, 8, 9]:
            return False
        return True

# 作者：powcai 转载
# 链接：https://leetcode-cn.com/problems/two-sum/solution/fan-ti-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution3:
    # 直接判断
    def isNumber(self, s: str):
        s = s.strip()
        #print(s)
        dot_seen = False
        e_seen = False
        num_seen = False
        for i, a in enumerate(s):
            if a.isdigit():
                num_seen = True
            elif a == ".":
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            elif a == "e":
                if e_seen or not num_seen:
                    return False
                num_seen = False
                e_seen = True
            elif a in "+-":
                if i > 0 and s[i - 1] != "e":
                    return False
            else:
                return False
        return num_seen