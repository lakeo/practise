# encoding=utf8

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    center = len(nums) // 2
    left = merge_sort(nums[0:center])
    right = merge_sort(nums[center:len(nums)+1])

    curr = []
    while len(left) != 0 or len(right) != 0:
        if left and right:
            if left[0] < right[0]:
                curr.append(left.pop(0))
            else:
                curr.append(right.pop(0))
        elif left:
            for i in left:
                curr.append(i)
            break
        elif right:
            for i in right:
                curr.append(i)
            break
    return curr


numbers = [2, 2, 2, 2, 133, 12, 2, 3, 4, 5, 2, 2, 9, 223, 4, 5, 1489, 24, 5, 2, 5, 70000, 80000, 10000]
print(numbers)
numbers = merge_sort(numbers)
print(numbers)
