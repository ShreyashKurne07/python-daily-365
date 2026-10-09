'''LeetCode 448: Find All Numbers Disappeared in an Array

Problem statement: You are given a list of length n where every value is between 1 and n. Some values appear twice and some 
don’t appear at all. Return a list of all numbers from 1 to n that are missing. This is the bigger version of LC 268.

Expected output:
[4, 3, 2, 7, 8, 2, 3, 1] -> [5, 6] (n is 8, so the range is 1 to 8, and 5 and 6 never appear)
[1, 1] -> [2]
[1, 2, 3] -> []
[2, 2, 2] -> [1, 3]'''

def disappearedArray(nums):
    listfinal = []
    n = len(nums)

    for i in range(1,n+1):
        if  i not in nums:
            listfinal.append(i)
    return listfinal

print(disappearedArray([4,3,2,7,8,2,3,1]))
print(disappearedArray([1, 1]))
print(disappearedArray([1, 2, 3]))
print(disappearedArray([2,2,2]))
