'''
Day 58: Filter Out a Value
Problem statement: Given a list of numbers and a target value, return a new list with all instances of that target value removed.
Input: [3, 2, 2, 3], target: 3 → Output: [2, 2]
'''

def remove_target(nums, target):

        result = []
        for i in nums:
                if i != target:
                        result.append(i)
        return result

print(remove_target([3, 2, 2, 3], 3))
print(remove_target([0, 1, 2, 2, 3, 0, 4, 2], 2))
