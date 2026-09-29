'''
LeetCode 485: Max Consecutive Ones

Problem statement: You are given a binary array, meaning a list that contains only 0s and 1s.
Return the length of the longest continuous run of 1s in the array.

Expected output:
[1, 1, 0, 1, 1, 1] -> 3 (the first run of 1s has length 2 and the last run has length 3, so 3 is the
 answer)
[1, 0, 1, 1, 0, 1] -> 2
[0, 0, 0] -> 0
[1, 1, 1, 1] -> 4
'''

def max_consecutive_ones(nums):
        max_count = 0
        current_count = 0

        for i in nums:
                if i == 1:
                        current_count = current_count + 1
                        if current_count > max_count:
                                max_count = current_count
                        else:
                                current_count = 0
        return max_count

print(max_consecutive_ones([1,1,0,1,1,1]))
print(max_consecutive_ones([1,0,1,1,0,1]))
print(max_consecutive_ones([0,0,0]))
