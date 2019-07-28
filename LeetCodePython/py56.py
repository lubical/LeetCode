# 合并区间； 排序后合并
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
     
        result = []
        intervals.sort()
        begin = intervals[0][0]
        end = intervals[0][1]
        for item_begin, item_end in intervals:
            if item_begin > end:  # 超出当前的边界，不能合并，则加入结果数组 
                result.append([begin, end])
                begin = item_begin
                end = item_end
            elif item_end > end:  # 不超出边界，则判断是否需要更新边界
                end = item_end
        result.append([begin, end]) # 最后一个边界加入
        return result