'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''



def shuffle(nums):
	insert_index = 0
	for i in nums:
		if i != 0:
			nums[insert_index] = i
			insert_index += 1
	for i in range(insert_index,len(nums)):
		nums[i] = 0



nums = [0,1,0,3,12]
shuffle(nums)
print(nums)
