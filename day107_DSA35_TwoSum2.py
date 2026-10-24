'''
LeetCode 167: Two Sum II - Input Array Is Sorted

Problem statement: You are given a list sorted in increasing order and a target. Find the two numbers that add up to target and return their positions as a list [i, j], with positions counted from 1, not 0. There is exactly one answer. Use O(1) extra space, so no dict.

Expected output:
[2, 7, 11, 15], target = 9 -> [1, 2] (2 + 7 = 9, and they sit at positions 1 and 2 when counting from 1)
[2, 3, 4], target = 6 -> [1, 3]
[-1, 0], target = -1 -> [1, 2]
[1, 2, 3, 4, 4, 9, 56, 90], target = 8 -> [4, 5]
'''
def twoSum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
print(twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))
