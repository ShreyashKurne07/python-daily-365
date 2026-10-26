'''
LeetCode 905: Sort Array By Parity

Problem statement: You are given a list of numbers. Rearrange it in place so that all even numbers come before all odd numbers, 
and return the list. The order inside the evens and inside the odds does not matter. Use O(1) extra space.

Expected output (any order with evens first is accepted):
[3, 1, 2, 4] -> [4, 2, 1, 3] (2 and 4 are even so they come first; [2, 4, 3, 1] would also be correct)
[0] -> [0]
[1, 3, 5] -> [1, 3, 5]
[2, 4, 1] -> [2, 4, 1]
'''

def sortedArraybyParity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left]%2 == 0:
            left+=1
        elif nums[right]%2 !=0:
            right -= 1

        else:
            nums[right],nums[left] = nums[left],nums[right]
    return nums

print(sortedArraybyParity([3,1,2,4]))
print(sortedArraybyParity([0]))
print(sortedArraybyParity([1,3,5]))
print(sortedArraybyParity([2,4,1]))
