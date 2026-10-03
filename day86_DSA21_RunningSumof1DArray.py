'''Problem 1: LeetCode 1480: Running Sum of 1d Array

Problem statement: You are given a list of numbers. Return a list where each position holds the sum of all numbers from the start up to and including that position.

Expected output:
[1, 2, 3, 4] -> [1, 3, 6, 10] (1, then 1+2, then 1+2+3, then 1+2+3+4)
[1, 1, 1, 1, 1] -> [1, 2, 3, 4, 5]
[3, 1, 2, 10, 1] -> [3, 4, 6, 16, 17]
[5] -> [5]'''

def listofNumbers(nums):
    list1 = []
    running_sum = 0

    for i in nums:
        running_sum = running_sum+int(i)
        list1.append(running_sum)
    return list1
print(listofNumbers([1,2,3,4]))
print(listofNumbers([1,1,1,1,1]))
print(listofNumbers([3,1,2,10,1]))
print(listofNumbers([5]))
