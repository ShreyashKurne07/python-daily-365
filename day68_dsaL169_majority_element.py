'''
Leetcode 169
Given an array of size n, return the element that appears more than n/2 times. You may assume it always exists.


Input:  [3,2,3]           → Output: 3
Input:  [2,2,1,1,1,2,2]   → Output: 2
Input:  [1]               → Output: 1
Your dict-counting pattern solves this directly. Do that version first.
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
print(majority_element([1]))
