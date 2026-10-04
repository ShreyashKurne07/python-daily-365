'''
LeetCode 1672: Richest Customer Wealth

Problem statement: You are given a list of lists. Each inner list is one customer's bank accounts, and each number is the money in
 that account. A customer's wealth is the sum of all their accounts. Return the wealth of the richest customer.

Expected output:
[[1, 2, 3], [3, 2, 1]] -> 6 (customer 1 has 1+2+3=6, customer 2 has 3+2+1=6, richest is 6)
[[1, 5], [7, 3], [3, 5]] -> 10
[[2, 8, 7], [7, 1, 3], [1, 9, 5]] -> 17
[[10]] -> 10
'''

def richestCustomer(list1):
    max_wealth = 0

    for i in list1:
        x = sum(i)
        if x > max_wealth:
            max_wealth = x
    return max_wealth
print(richestCustomer([[1, 2, 3], [3, 2, 1]]))
print(richestCustomer([[1, 5], [7, 3], [3, 5]]))
print(richestCustomer([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
print(richestCustomer([[10]]))
