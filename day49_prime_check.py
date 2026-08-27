'''
Day 49 — 27 Aug (Thu) (PAPER DAY — 10 min max)

Problem: Check whether a given number is prime. Return True or False.

Input:  7    → Output: True
Input:  10   → Output: False
Input:  1    → Output: False
Input:  2    → Output: True
'''

def is_prime(num):
        if num <= 1:
                return False

        for i in range(2, num):
                if num % i == 0:
                        return False

        return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(1))
print(is_prime(2))
