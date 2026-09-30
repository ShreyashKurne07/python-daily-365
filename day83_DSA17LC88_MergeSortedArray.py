'''
LeetCode 88: Merge Sorted Array

Problem statement: You get two lists, nums1 and nums2, both sorted in increasing order, plus two numbers m and n. The first m 
elements of nums1 are real values. Its total length is m + n, and the last n slots are 0s used as empty space. nums2 has exactly n 
elements. Merge nums2 into nums1 so that nums1 becomes one sorted list. Do it in place inside nums1 and don't return anything. '
'Don't use sort(), because an interviewer will reject that.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''
'''Merge sort logic asa ahe ki 3 pointer ahet pahila
real end of nums1 dusra end of nums2 tisra end of nums1 
mag aplyala pointer magun pudhe nyachay compare karat ani element add karaychay
'''
'''
LeetCode 88: Merge Sorted Array

Problem statement: You get two lists, nums1 and nums2, both sorted in increasing order, plus two numbers m and n. The first m 
elements of nums1 are real values. Its total length is m + n, and the last n slots are 0s used as empty space. nums2 has exactly n 
elements. Merge nums2 into nums1 so that nums1 becomes one sorted list. Do it in place inside nums1 and don't return anything. '
'Don't use sort(), because an interviewer will reject that.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''
'''Merge sort logic asa ahe ki 3 pointer ahet pahila
real end of nums1 dusra end of nums2 tisra end of nums1 
mag aplyala pointer magun pudhe nyachay compare karat ani element add karaychay
'''
def mergeSort(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 = p1 - 1
        else:
            nums1[p] = nums2[p2]
            p2 = p2 - 1
        p = p - 1
            
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 = p2 - 1
        p = p - 1

nums1 = [1, 2, 3, 0, 0, 0]
mergeSort(nums1, 3, [2, 5, 6], 3)
print(nums1)

nums2 = [1]
mergeSort(nums2, 1, [], 0)
print(nums2)

nums3 = [0]
mergeSort(nums3, 0, [1], 1)
print(nums3)

nums4 = [2, 0]
mergeSort(nums4, 1, [1], 1)
print(nums4)
