'''LeetCode 724: Find Pivot Index

Problem statement: You are given a list of numbers. Find an index where the sum of all numbers strictly to its left equals the sum
of all numbers strictly to its right. The number at that index itself is not counted on either side. If there is more than one
such index, return the leftmost one. If there is none, return -1. If nothing is on one side, that side's sum is 0.

Expected output:
[1, 7, 3, 6, 5, 6] -> 3 (at index 3, left is 1+7+3 = 11 and right is 5+6 = 11)
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0] -> 0'''

def findPivot(numbers):
    left_sum = 0
    total_sum =sum(numbers)
    for i in range(len(numbers)):
        right_sum = total_sum - left_sum - numbers[i]
        if left_sum==right_sum:
            return i
        left_sum+=numbers[i]
    return -1

print(findPivot([1,7,3,6,5,6]))
print(findPivot([1,2,3]))
print(findPivot([2,1,-1]))
print(findPivot([0]))
