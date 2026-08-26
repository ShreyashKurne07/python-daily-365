'''
Problem: Given two lists, return a list of elements common to both. Keep the order of the first list, and no repeats in the answer.

Input:  [1,2,3,4,5], [4,5,6,7]      → Output: [4, 5]
Input:  [1,2,2,3], [2,3]            → Output: [2, 3]
Input:  [1,2], [8,9]                → Output: []
'''

def find_common(list1, list2):
        common = []

        for i in list1:
                if i in list2 and i not in common:
                        common.append(i)
        return common

print(find_common([1, 2, 3, 4, 5], [4, 5, 6, 7]))
print(find_common([1, 2, 2, 3], [2, 3]))
print(find_common([1, 2], [8, 9]))
