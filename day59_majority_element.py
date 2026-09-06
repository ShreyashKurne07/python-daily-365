'''
Day 59: Find the Majority Element
Problem statement: Given a list, find the element that appears more than half the time (you can assume one always exists).
Input: [2, 2, 1, 1, 1, 2, 2] → Output: 2
'''

def majority_element(nums):

        counts = {}
        for i in nums:
                if i in counts:
                        counts[i] = counts[i] + 1
                else:
                        counts[i] = 1
        half = len(nums) / 2
        for i in counts:
                if counts[i] > half:
                        return i

print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
