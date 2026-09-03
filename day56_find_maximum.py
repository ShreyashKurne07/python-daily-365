'''
Day 56: Find the Maximum Number
Problem statement: Given a list of numbers, find the largest number without using the built-in max() function.
Input: [3, 8, 1, 9, 4] → Output: 9
'''

def find_maximum(nums):

        biggest = nums[0]
        for i in nums:
                if i > biggest:
                        biggest = i
        return biggest

print(find_maximum([3, 8, 1, 9, 4]))
print(find_maximum([-5, -2, -10]))
