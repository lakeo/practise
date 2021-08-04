# encoding=utf8

def bubble_sort(nums):
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]


numbers = [2, 2, 2, 2, 133, 12, 2, 3, 4, 5, 2, 2, 9, 223, 4, 5, 1489, 24, 5, 2, 5, 70000, 80000, 10000]
print(numbers)
bubble_sort(numbers)
print(numbers)
