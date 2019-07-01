# Z字变换，模拟
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for i in range(numRows)]
      
        direction = 1
        index = 0
        for ch in s:
            result[index].append(ch)
            index = index + direction
            if index == numRows or index == -1:
                direction = - direction
                index = direction*2+index
     
        result = ["".join(item) for item in result]
        result = "".join(result)
        return result
                
                
        