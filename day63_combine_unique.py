'''
Day 63: Union of Two Lists
Problem statement: Given two lists, combine them into one list, but ensure there are no duplicate numbers in the final result.
Input: [1, 2, 3], [3, 4, 5] → Output: [1, 2, 3, 4, 5]
'''

def combine_unique(list1, list2):

        result = []

        for i in list1:
                if i not in result:
                        result.append(i)
        for i in list2:
                if i not in result:
                        result.append(i)
        return result

print(combine_unique([1, 2, 3], [3, 4, 5]))
print(combine_unique([1, 1], [1, 2]))
