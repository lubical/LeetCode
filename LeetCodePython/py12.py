class Solution:
    #解法二：进制处理。最大优先
    def intToRoman(self, num: int) -> str:
        lookup = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'  
        }
        result = ""
        for key in sorted(lookup.keys())[::-1]:
            items = num//key
            if items == 0:
                continue
            result += lookup[key]*items
            num -= items * key
        return result


class Solution1:
    # 解法一：暴力动态规划，以num数值建立数组
    def intToRoman(self, num: int) -> str:
        value = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        label = ['I','IV','V','IX','X','XL','L', 'XC', 'C','CD','D','CM', 'M']
        dp = [False] * (num + 1)
        dp[0] = True
        result = [''] * (num + 1)
        for i in range(num+1):
            for j in range(len(value)-1, -1, -1):
                if dp[i] and i+value[j]< num+1 and not dp[i+value[j]]:
                    dp[i+value[j]] = True
                    result[i+value[j]] = label[j] + result[i]
        # for i in range(num):
        #     print(dp[i], result[i])
        return result[num]
        
       
        
        
        