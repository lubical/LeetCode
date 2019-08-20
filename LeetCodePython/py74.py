# 探索矩阵
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 解法 二分
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n==0:
            return False
        m = len(matrix[0])
        left = 0
        right = n * m - 1
        while left<=right:
            mid = (left+right)>>1
            pivot_element = matrix[mid // m][mid % m]
            if pivot_element > target:
                right = mid - 1
            elif pivot_element < target:
                left = mid + 1
            else:
                return True
        return False