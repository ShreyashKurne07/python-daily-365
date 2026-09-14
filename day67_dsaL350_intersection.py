'''
Problem 1 — LeetCode 350: Intersection of Two Arrays II (Easy)
Problem statement:

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays. The result can be in any order.
Expected output:


Input:  nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]   (or [9,4])

Input:  nums1 = [1,2], nums2 = [3,4]
Output: []
'''


def intersect(nums1, nums2):
        counts = {}
        result = []

        for i in nums1:
                if i in counts:
                        counts[i] = counts[i] + 1
                else:
                        counts[i] = 1

        for i in nums2:
                if i in counts and counts[i] > 0:
                        result.append(i)
                        counts[i] = counts[i] - 1
        return result

print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersect([1, 2], [3, 4]))
