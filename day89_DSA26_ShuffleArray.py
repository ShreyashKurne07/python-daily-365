'''Problem 1: LeetCode 1470: Shuffle the Array

Problem statement: You are given a list nums of length 2n and the number n. The first half is x1, x2, ..., xn and the second half
is y1, y2, ..., yn. Return a new list in the order x1, y1, x2, y2, ..., xn, yn.

Expected output:
nums = [2, 5, 1, 3, 4, 7], n = 3 -> [2, 3, 5, 4, 1, 7] (the x values are 2, 5, 1 and the y values are 3, 4, 7, so pairing them 
gives 2,3 then 5,4 then 1,7)
nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4 -> [1, 4, 2, 3, 3, 2, 4, 1]
nums = [1, 1, 2, 2], n = 2 -> [1, 2, 1, 2]
nums = [7, 9], n = 1 -> [7, 9]'''

def shuffleArray(nums,n):
    list3 = []
    list1 = nums[:n]
    list2 = nums[n:]
    for i in range(n):
        list3.append(list1[i])
        list3.append(list2[i])

    return list3

print(shuffleArray([2,5,1,3,4,7],3))
print(shuffleArray([1,2,3,4,4,3,2,1],4))
print(shuffleArray([1,1,2,2],2))
print(shuffleArray([7,9],1))
