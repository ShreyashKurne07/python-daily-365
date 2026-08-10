#Example 2:

#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).






def removeduplicates(self,nums):
	insert_index = 1
	for i in range(1,len(nums)):
		if (nums[i] != nums[i-1]):
			nums[insert_index] = nums[i]
			insert_index += 1
	return insert_index

nums = [1,1,2]
print(removeduplicates(None, nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeduplicates(None, nums))
