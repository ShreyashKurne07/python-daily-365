'''
Problem: Given a list of numbers, return a new list with duplicates removed, keeping the original order.


Input:  [3,1,3,5,1,9]   → Output: [3, 1, 5, 9]
Input:  [1,1,1]         → Output: [1]
Input:  []              → Output: []
'''

def remove_duplicates(nums):

        result = []
        for i in nums:
                if i not in result:
                        result.append(i)
        return result
print(remove_duplicates([3, 1, 3, 5, 1, 9]))
print(remove_duplicates([1, 1, 1]))
print(remove_duplicates([]))
