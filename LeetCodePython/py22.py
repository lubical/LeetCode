# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
from typing import List
class Solution:
    # 生成写法，在n-1对正确的基础上，枚举每一个字符串的每一个位置插入一对括号，并加入集合去重
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        
        pre = set({'()',})
        
        for i in range(n-1):
            now = set()
            for st in pre:
                n = len(st)
                for index in range(n):
                    now.add(st[0:index]+'()'+st[index:n])
            pre = now
        return list(pre)