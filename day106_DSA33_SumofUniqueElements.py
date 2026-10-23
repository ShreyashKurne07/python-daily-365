'''
Problem 1: LeetCode 1748: Sum of Unique Elements

Problem statement: You are given a list of numbers. Return the sum of the numbers that appear exactly once.

Expected output:
[1, 2, 3, 2] -> 4 (2 appears twice, so only 1 + 3 is added)
[1, 1, 1, 1, 1] -> 0
[1, 2, 3, 4, 5] -> 15
[7] -> 7'''

def sumUniqueElements(nums):
    addition = []


    for i in nums:
        counter = 0
        for j in nums:
            if i == j:
                counter+=1
                
        if counter == 1:
            addition.append(i)
    return sum(addition)

print(sumUniqueElements([1,2,3,2]))
print(sumUniqueElements([1,1,1,1,1]))
print(sumUniqueElements([1,2,3,4,5]))
print(sumUniqueElements([7]))


