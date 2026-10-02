'''
LeetCode 1342: Number of Steps to Reduce a Number to Zero

Problem statement: You are given a non-negative integer num. Count how many steps it takes to make it 0. In each step,
if the number is even, divide it by 2. If it is odd, subtract 1. Return the number of steps.

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
'''
def steps_reducetoZero(num):
    count = 0
    current = num
    
    while num > 0:
        if (num % 2 == 0):
            count+= 1
            current = num//2
            num = current
        
        else:
            count+=1
            current = num -1
            num = current
    return count


print(steps_reducetoZero(14))
print(steps_reducetoZero(8))
print(steps_reducetoZero(123))
print(steps_reducetoZero(0))

