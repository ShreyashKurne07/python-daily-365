'''
LeetCode 27 — Remove Element (Easy)

Problem statement:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of remaining elements can change. Return the count k of elements that are not equal to val. The first k positions of nums must hold those elements.

Expected output:

Input:  nums = [3,2,2,3], val = 3
Output: 2,  nums first 2 positions = [2,2]

Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5,  nums first 5 positions = [0,1,3,0,4]

Input:  nums = [1], val = 1
Output: 0
'''

def remove_element(nums, val):
        k = 0
        
        for i in nums:
                if i != val:
                        nums[k] = i
                        k = k + 1
                        
        return k

nums1 = [3, 2, 2, 3]
k1 = remove_element(nums1, 3)
print(k1)
print(nums1[:k1]) 

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = remove_element(nums2, 2)
print(k2)
print(nums2[:k2]) 

nums3 = [1]
k3 = remove_element(nums3, 1)
print(k3)
print(nums3[:k3])
