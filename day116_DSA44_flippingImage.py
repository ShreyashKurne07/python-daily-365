'''2Nov
LeetCode 832: Flipping an Image

Problem statement: You are given a square grid (a list of lists) of 0s and 1s. For each row, first reverse the row, 
then flip every value (0 becomes 1 and 1 becomes 0). Return the grid. Do it in place, without [::-1] or reverse().
First reverse all then inverse
Expected output:
[[1,1,0],[1,0,1],[0,0,0]] -> [[1,0,0],[0,1,0],[1,1,1]] (the first row [1,1,0] reversed is [0,1,1], and flipped it is [1,0,0])
[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] -> [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
[[1]] -> [[0]]
[[0,1],[1,1]] -> [[0,1],[0,0]]'''

def flippingImage(list1):
    for i in list1:
        left = 0
        right = len(i) - 1
        while left < right:
            i[left], i[right] = i[right], i[left]
            left += 1
            right -= 1
        for j in range(len(i)):
            if i[j] == 0:
                i[j] = 1
            else:
                i[j] = 0
    return list1

print(flippingImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flippingImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
print(flippingImage([[1]]))
print(flippingImage([[0,1],[1,1]]))

