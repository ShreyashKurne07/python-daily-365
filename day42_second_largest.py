'''
Write a program that takes a list of numbers and returns the second largest number in the list, 
without using sort() or max().

Input:  [4, 1, 7, 3, 7, 2]
Output: 7   (largest, appears twice → second largest is still 7)

Input:  [10, 20, 4, 45, 99]
Output: 45

Input:  [5, 5, 5]
Output: 5
'''

def secondlargest(nums):
	largest_no = -9999
	second_largest = -9999
	list1 = nums.copy()
	for i in list1:
		if i > largest_no:
			largest_no = i
	list1.remove(largest_no)
	for i in list1:
		if i > second_largest:
			second_largest = i
	return ("Output: ",second_largest)

print(secondlargest([4,1,7,3,7,2]))
print(secondlargest([10,20,4,45,99]))

