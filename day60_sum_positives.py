'''
Day 60: Sum of Positive Numbers
Problem statement: Given a list of numbers, return the sum of all positive numbers. Ignore negatives and zeros.
Input: [1, -4, 7, 12] → Output: 20
'''

def sum_positives(nums):

        total = 0
        for i in nums:
                if i > 0:
                        total = total + i
        return total

print(sum_positives([1, -4, 7, 12]))
print(sum_positives([-1, -2, -3]))
