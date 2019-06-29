from typing import List
class Solution:
    # 题目描述：两个有序数组，假设同时递增或同时递减，找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))
    # 简单的做法是 直接排序，O(n+m)可完成，改进点：不需要真的排序，找到相应位置即可
    # 满足O(log(m+n))的解法是假设在两个数组中间割一刀（左边个数总和为总数一半），若左半边全部小于右半边，则满足条件，
    #     因此，可以二分最短的数组，每次保证数组一与数组二左边数目和为总数一半，交叉判断切割点值。
    #     特殊情况，第一个数组左端为空，说明第一个数组都大于中位数，中位数在数组二；
    #             第一个数组右端为空，说明第一个数组都小于中位数，中位数在数组二；
    #             第二个数组左端为空，说明第二个数组都大于中位数，中位数在数组一；
    #             第二个数组右端为空，说明第二个数组都小于中位数，中位数在数组一；
    #     小技巧：虚拟数组[1,2,3]->[#,1,#,2,#,3,#]扩充为2*n+1，实际对应整除2即可得到原来的位置
    #            切割点定位于数字上，则在#则数字之间，在数字则数字分别拆分到左右两边。
    #            定位关系 a1,a2,a3...,lmax1,rmin1,aj,aj+1,...
    #            lmaxi = (cuti-1)//2; rmini = cuti//2;
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:  # 遍历短的加快速度
            return self.findMedianSortedArrays(nums2,nums1)
        
        cut1,cut2 = 0, 0
        lMax1,lMax2 = 0, 0
        rMin1,rMin2 = 0, 0
        low = 0
        high = n * 2  # 虚拟数组，长度变为2*n+1
        while low <= high:  # 此处要有=，因为第一个可能为空
            cut1 = (low + high) >> 1
            cut2 = n + m - cut1
            lMax1 = float('-Inf') if cut1 == 0 else nums1[(cut1-1)>>1]
            rMin1 = float('Inf') if cut1 == 2*n else nums1[cut1>>1]
            lMax2 = float('-Inf') if cut2 == 0 else nums2[(cut2-1)>>1]
            rMin2 = float('Inf') if cut2 == 2*m else nums2[cut2>>1]
            if lMax1 > rMin2:  # 割1太大了
                high = cut1 - 1
            elif lMax2 > rMin1:  # 割2太大，即割1太小
                low = cut1 + 1
            else:  # 刚好是所求位置
                break
        return (max(lMax1, lMax2) + min(rMin1, rMin2))/2
            
        
            
        
        