from typing import List
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
# 单词可重复
class Solution:
    # 两个字典，一个用来处理所有单词及其个数，另一个用来枚举时判断使用
    def findSubstring(self, s: str, words: List[str]) -> List[int]:  
        if not words:
            return []
        
        old_dict = {}
        n = len(words[0])
        
        if len(s) < n * len(words):
            return []
  
        for word in words:  # 用字典可以处理有重复的子串
            if word not in old_dict:
                old_dict[word] = 1
            else:
                old_dict[word] += 1
            
        result = []
        for i in range(len(s) - n*len(words)+1):
            new_dict = {}  # 原来想用减法，初值为old_dict,复制比较慢，改成加法后快多了。
            find = 1
            for j in range(len(words)):
                subs = s[i+j*n:i+(j+1)*n]
                if subs in old_dict and old_dict.get(subs,0) > new_dict.get(subs,0):
                    if subs in new_dict:
                        new_dict[subs] += 1
                    else:
                        new_dict[subs] = 1
                else:
                    find = 0
                    break
            if find:
                result.append(i)
        return result
            
            