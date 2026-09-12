'''
Day 65: Find All Duplicates
Problem statement: Given an array of integers, return a list of all the numbers that appear exactly twice.
Input: [4, 3, 2, 7, 8, 2, 3, 1] → Output: [2, 3]
'''

def find_all_duplicates(nums):

        counts = {}
        result = []
        for i in nums:
                if i in counts:
                        counts[i] = counts[i] + 1
                else:
                        counts[i] = 1
        for i in counts:
                if counts[i] == 2:
                        result.append(i)
        return result

print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_all_duplicates([1, 2, 3]))
