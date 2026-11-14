'''
LeetCode 11: Container With Most Water (your first Easy-Medium)

Problem statement: You are given a list height, where each number is the height of a vertical line at that position. Pick two line
s. Together with the x-axis they hold water, and the amount is (distance between them) × (height of the shorter line). 
Return the maximum water possible. A nested-loop O(n²) solution is fine as a first attempt, but the target is O(n).

Expected output:
[1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 (lines at positions 1 and 8 have heights 8 and 7, so 7 × 7 = 49)
[1, 1] -> 1
[4, 3, 2, 1, 4] -> 16
[1, 2, 1] -> 2'''

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_water = width * current_height
        if current_water > max_water:
            max_water = current_water
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([4, 3, 2, 1, 4]))
print(maxArea([1, 2, 1]))
