'''
LeetCode 268: Missing Number
Problem statement: You are given a list nums containing n distinct numbers, each taken from the
 range 0 to n. Exactly one number from that range is missing. Find and return that missing 
 number.

Expected output:
[3, 0, 1] -> 2 (range is 0 to 3, number 2 is missing)
[0, 1] -> 2 (range is 0 to 2, number 2 is missing)
[9, 6, 4, 2, 3, 5, 7, 0, 1] -> 8
[0] -> 1
'''

def missing_number(nums):
    seen = {}

    for num in nums:
        seen[num] = 1

    for number in range(len(nums)+1):
        if number not in seen:
            return number

print(missing_number([3,0,1]))
print(missing_number([0,1]))
print(missing_number([9,6,4,2,3,5,7,0,1]))
print(missing_number([0]))
