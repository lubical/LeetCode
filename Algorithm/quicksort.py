from typing import List
def quicksort1(nums: List[int], left: int, right: int) -> None:
    if left>=right:
        return
    i, j = left, right
    mid = (left+right)//2
    key = nums[mid]
    while 1:
        while i < right and nums[i] < key:
            i += 1
        while left < j and nums[j] > key:
            j -= 1

        if i>=j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
        j-=1

    quicksort1(nums, left, i-1)
    quicksort1(nums, j+1, right)

def quicksort(nums: List[int], left: int, right: int) -> None:
    if left>=right:
        return
    i, j = left, right
    key = nums[left]
    while i<j:
        while i < j and nums[j] > key: j-=1
        nums[i] = nums[j]
        while i < j and nums[i] < key: i += 1
        nums[j] = nums[i]
    nums[i] = key
    quicksort(nums, left, j-1)
    quicksort(nums, i+1, right)


def quicksort3(nums: List[int], left: int, right: int) -> None:
    if left>=right:
        return
    key = nums[left]
    start = left + 1
    for i in range(left, right+1):
        if nums[i]< key:
            nums[i],nums[start] = nums[start], nums[i]
            start += 1
    nums[left], nums[start-1] = nums[start-1], nums[left]
    # 因为第一个数固定了，且从第一个数到第start都是小于第一个数的
    quicksort3(nums, left, start-1)
    quicksort3(nums, start, right)
# nums = [8,2,6,3,3,3,3,4,5]
# quicksort(nums, 0, len(nums)-1)
# print(nums)

nums = [8,2,6,3,3,3,3,4,5]
quicksort3(nums, 0, len(nums)-1)
print(nums)