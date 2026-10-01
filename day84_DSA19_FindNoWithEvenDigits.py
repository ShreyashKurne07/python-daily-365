'''
LeetCode 1295: Find Numbers with Even Number of Digits
Problem statement: You are given a list of positive integers. Count how many of them have an even number of digits, and return 
that count.

Expected output:
[12, 345, 2, 6, 7896] -> 2 (12 has 2 digits and 7896 has 4 digits, both even; the others have 3, 1 and 1 digits)
[555, 901, 482, 1771] -> 1
[1, 2, 3] -> 0
[10, 100, 1000] -> 2
'''
def even_digits(nums):

    count = 0
    for number in nums:

        length = len(str(number))

        if length % 2 == 0:
            count = count+1
    return count

print(even_digits([12,345,2,6,7896]))
print(even_digits([555,901,482,1771]))
print(even_digits([1,2,3]))
print(even_digits([10,100,1000]))
