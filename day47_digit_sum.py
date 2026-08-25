'''
Problem: Find the sum of digits of a positive number.

Input:  12345   → Output: 15
Input:  909     → Output: 18
Input:  7       → Output: 7

'''
def sum_of_digits(num):

        total = 0
        num_str = str(num)
        for i in num_str:
                total = total + int(i)
        return total
print(sum_of_digits(12345))
print(sum_of_digits(909))
print(sum_of_digits(7))
