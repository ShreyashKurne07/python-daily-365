'''
Given an integer array nums, return True if any value appears at least twice in the array. 
Return False if every element is distinct.

Input:  nums = [1, 2, 3, 1]
Output: True
(1 appears twice)

Input:  nums = [1, 2, 3, 4]
Output: False
(all distinct)

Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
'''


def containduplicates(nums):
	word_counts = {}
	for i in nums:
		if i in word_counts:
			return True

		else:
			word_counts[i] = 1

	return False

print(containduplicates([1,2,3,1]))
print(containduplicates([1,2,3,4]))

