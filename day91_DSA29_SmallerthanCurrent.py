'''LeetCode 1365: How Many Numbers Are Smaller Than the Current Number

Problem statement: You are given a list of numbers. For each number, count how many other numbers in the list are strictly smaller
 than it. Return a list of these counts in the same order.

Expected output:
[8, 1, 2, 2, 3] -> [4, 0, 1, 1, 3] (for 8, the smaller numbers are 1, 2, 2, 3, so 4)
[6, 5, 4, 8] -> [2, 1, 0, 3]
[7, 7, 7, 7] -> [0, 0, 0, 0]
[5] -> [0]'''

def smallerThanCurrent(nums):
    listfinal = []

    for i in nums:
        counter = 0
        for j in nums:
            if i > j:
                counter += 1
        listfinal.append(counter)
    return listfinal

print(smallerThanCurrent([8,1,2,2,3]))
print(smallerThanCurrent([6,5,4,8]))
print(smallerThanCurrent([7,7,7,7]))
print(smallerThanCurrent([5]))


