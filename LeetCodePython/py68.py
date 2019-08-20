# 文本左右对齐；最后一行左对齐且不插入额外的空格。
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current = []
        current_len = -1  # 每个单词要间要有一个空格，只有一个单词则可以不需要空格，所以从-1开始。
        for pos,word in enumerate(words):
            if current_len + len(word) + 1 > maxWidth:  # 单词间至少要有一个空格
                space_len = maxWidth - current_len  # 包含了预先加入的一个空格
                word_count = len(current) - 1
                if word_count == 0:
                    result.append(current[0]+" "*(maxWidth-len(current[0])))
                    current.clear()
                    current.append(word)
                    current_len = len(word)
                    continue
                space_add = [" "] * word_count
                space_each = space_len // word_count
                space_left = space_len % word_count
                for i in range(len(space_add)):
                    space_add[i] += " "*space_each
                    space_add[i] += " " if space_left>0 else ""
                    space_left -= 1
                
                temp = ""
                for i in range(len(space_add)):
                    temp += current[i] + space_add[i]
                temp += current[-1]
                result.append(temp)
                
                current.clear()
                current.append(word)
                current_len = len(word)
                
            else:
                current_len += len(word) + 1
                current.append(word)
        
        temp = ""
        for word in current:
            temp += word + " "
        temp += " "*maxWidth
        temp = temp[0:maxWidth]
        result.append(temp)
        return result