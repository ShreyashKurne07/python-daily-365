'''
DSA — LeetCode 136, Single Number (Easy) (carried from 17 Aug)

Given a non-empty array where every element appears twice except one, find that single element.

Input:  [2,2,1]        → Output: 1
Input:  [4,1,2,1,2]    → Output: 4
Input:  [1]            → Output: 1
'''

def single_number(nums):

        counts = {}

        for i in nums:
                if i in counts:
                        counts[i] = counts[i] + 1
                else:
                        counts[i] = 1
        for i in counts:
                if counts[i] == 1:
                        return i
print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))
