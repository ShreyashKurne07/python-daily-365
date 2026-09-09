'''
Day 62: Custom String Length
Problem statement: Calculate the length of a string without using the built-in len() function.
Input: "hello" → Output: 5
'''

def custom_length(s):

        count = 0
        for i in s:
                count = count + 1
        return count

print(custom_length("hello"))
print(custom_length(""))
