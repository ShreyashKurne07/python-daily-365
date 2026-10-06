'''LeetCode 414: Third Maximum Number

Problem statement: You are given a list of numbers. Return the third largest distinct value, which means duplicates count only 
once. If there is no third distinct value, return the largest value. Don't use sort(). This is the bigger version of your Second 
Largest problem (#7 in your log).

Expected output:
[3, 2, 1] -> 1 (the distinct values are 3, 2, 1, so the third largest is 1)
[1, 2] -> 2 (only 2 distinct values, so return the largest)
[2, 2, 3, 1] -> 1 (the distinct values are 3, 2, 1, so the duplicate 2 counts once)
[5, 5, 5] -> 5'''

def thirdMax(nums):
    # Set our trackers to the lowest possible number initially
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    
    for num in nums:
        # Ignore duplicates - if we've already seen this exact number, skip it
        if num == first or num == second or num == third:
            continue
            
        # The Waterfall: shift values down if a new max is found
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
            
    # If 'third' was never updated, it means we had less than 3 unique numbers
    if third != float('-inf'):
        return third
    else:
        return first

print(thirdMax([3, 2, 1]))
print(thirdMax([1, 2]))
print(thirdMax([2, 2, 3, 1]))
print(thirdMax([5, 5, 5]))
