# 报数，模拟
class Solution:
    def countAndSay(self, n: int) -> str:
        import re
        def helper(answer, n):
            if n-1 == 0:
                return answer
            else:
                result = [str(len(item[0]))+item[1] for item in re.findall(r'((\d)\2*)', answer)] 
                # (\d) 组号是2，匹配的结果比如"111",("111","1"), r'((\d)\2*)'有两个分组，第一个分组匹配最外层，第二个分组匹配\d
                return helper("".join(result), n-1)
        
        return helper("1", n)