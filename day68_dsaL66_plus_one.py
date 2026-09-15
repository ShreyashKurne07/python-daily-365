'''
Problem 1 — LeetCode 66: Plus One (Easy)
Given a non-empty array of digits representing a large integer (most significant digit first), increment the integer by one and return the resulting digit array.


Input:  [1,2,3]     → Output: [1,2,4]
Input:  [4,3,2,9]   → Output: [4,3,3,0]
Input:  [9,9]       → Output: [1,0,0]
Input:  [0]         → Output: [1]
Watch out: the all-nines case. The answer array gets longer than the input. 
Think about that before you write.
'''

def plus_one(digits):
        num_str = ""

        for i in digits:
                num_str = num_str + str(i)

        total = int(num_str) + 1
        total_str = str(total)

        result = []
        for i in total_str:
                result.append(int(i))
        return result

print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 9]))
print(plus_one([9, 9]))
print(plus_one([0]))
