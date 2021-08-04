# encoding=utf8
import random


def quick_sort(nums, begin, end):
    left = begin
    right = end
    if left >= right:
        return
    tmp = nums[left]
    while left < right:
        while nums[right] >= tmp and left < right:
            right -= 1
        while nums[left] < tmp and left < right:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    quick_sort(nums, begin, left)
    quick_sort(nums, left+1, end)


def quick_sort_v2(nums, begin, end):
    if begin >= end:
        return
    tmp = random.randint(begin, end)
    # 交换到最后
    nums[tmp], nums[end] = nums[end], nums[tmp]
    tmp = end
    right = end - 1
    left = begin

    while left < right:
        while nums[left] <= nums[tmp] and left < right:
            left += 1
        while nums[right] >= nums[tmp] and left < right:
            right -= 1
        if left < right:
            nums[left] , nums[right] = nums[right], nums[left]
    if nums[tmp] < nums[left]:
        nums[tmp], nums[left] = nums[left], nums[tmp]
    quick_sort_v2(nums, begin, left-1)
    quick_sort_v2(nums, left+1, end)



numbers = [2,2,2,2,133, 12,2,3,4,5,2,2,9,223,4,5,1489,24,5,2,5,70000,80000,10000]
# numbers = [3, 2, 1]
print(numbers)
quick_sort_v2(numbers, 0, len(numbers)-1)
print(numbers)
