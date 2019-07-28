# 插入区间，无重叠，按区间起始端点排序的区间插入一个新区间后仍然要求有序不重叠
# 下面的解法是将插入节点与剩下部分混合判断, 要修改，左端点比原来的小，左端点比原来的大，插入后后端点正好又是某个端点的起点
# 也可以分成三部分，前面不需要插入的，中间插入改变的区间的起始结束点，剩下的部分
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = list()
        if not intervals:
            return [newInterval]
        index = 0
        n = len(intervals)
        while index<n and intervals[index][1] < newInterval[0]: # 找到可以插入的位置
            result.append(intervals[index])
            index += 1
        if index == n:  # 已经是结尾，直接插入到末尾 
            result.append(newInterval)
            return result
        if index == 0 and intervals[index][0] > newInterval[1] or newInterval[1] < intervals[index][0]: # 不需要合并区间的两种情况，1，在开头；2，在中间
            result.append(newInterval)
            result.extend(intervals[index:])
            return result
        
        begin = min(intervals[index][0], newInterval[0]) # 再合并插入的新区间
        end = intervals[index][1]
        for j in range(index, n):
            if intervals[j][1] < newInterval[1]:  # 是否需要合并区间 
                end = newInterval[1]
            elif intervals[j][0] <= newInterval[1]:  # 判断是否插入后需要再合并
                end = intervals[j][1]
            else:  # 插入之后的每一个值
                result.append([begin, end])
                begin,end = intervals[j][0], intervals[j][1]
        result.append([begin, end])
        return result
                