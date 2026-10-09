'''Leetcode 1512: Number of Good Pairs

Problem statement: You are given a list of numbers. A pair of positions (i, j) is “good” if the values at those positions are 
equal and i < j. Return how many good pairs there are.

Expected output:
[1, 2, 3, 1, 1, 3] -> 4 (the 1s at positions 0, 3, 4 make 3 pairs, and the 3s at positions 2, 5 make 1 pair)
[1, 1, 1, 1] -> 6
[1, 2, 3] -> 0
[5] -> 0'''

def goodPairs(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):

            if nums[i] == nums[j]:
                count +=1
    return count
print(goodPairs([1,2,3,1,1,3]))
print(goodPairs([1,1,1,1]))
print(goodPairs([1,2,3]))
print(goodPairs([5]))
