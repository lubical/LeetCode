# 跳跃游戏，用最少的步数跳到重点
class Solution(object):
    # 贪心，走最远
    def jump(self, nums):
        n = len(nums)
        count = 0
        index = 0
        if n==1:
            return 0
        while index+nums[index]<n-1:
            max_index = index
            for j in range(index+1, min(index+nums[index]+1, n)):
                if j + nums[j] >= max_index + nums[max_index]:
                    max_index = j
            index = max_index
            count += 1
        return count+1 # 最后一轮没走，所以要加1
 
        # while index<n-1:
        #     next_large = index + nums[index]  # 错误，默认当前步数比下一个步数多
        #     next_index = index + nums[index]
        #     if next_index >= n-1:
        #         return count+1
        #     for j in range(index+1, min(index+nums[index],n)):
        #         if j + nums[j] > next_large:
        #             print j, nums[j], j+nums[j], next_large
        #             next_large = j + nums[j]
        #             next_index = j
        #     #print next_index, next_large
        #     count += 1
        #     index = next_index
        # return count
        