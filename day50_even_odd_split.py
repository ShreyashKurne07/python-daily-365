'''
Problem: Split a list of numbers into evens and odds, returned as a dictionary with keys "even" and "odd".

Input:  [1,2,3,4,5,6]  → Output: {'even': [2,4,6], 'odd': [1,3,5]}
Input:  [2,4]          → Output: {'even': [2,4], 'odd': []}
Input:  []             → Output: {'even': [], 'odd': []}

File: day50_even_odd_split.py
'''

def split_even_odd(nums):
        result = {'even': [], 'odd': []}

        for i in nums:
                if i % 2 == 0:
                        result['even'].append(i)
                else:
                        result['odd'].append(i)
        return result

print(split_even_odd([1, 2, 3, 4, 5, 6]))
print(split_even_odd([2, 4]))
print(split_even_odd([]))
