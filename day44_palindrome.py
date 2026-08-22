'''
Write a function that checks whether a given string is a palindrome — 
reads the same forwards and backwards. Ignore case, and ignore spaces.

Input:  "madam"
Output: True

Input:  "Nurses Run"
Output: True
(ignore case and space → "nursesrun")

Input:  "hello"
Output: False

Input:  "A man a plan a canal Panama"
Output: True
'''

def is_palindrome(s):

        s = s.lower()
        s = s.replace(" ", "")

        reversed_s = ""
        for i in s:
                reversed_s = i + reversed_s

        if s == reversed_s:
                return True
        else:
                return False

print(is_palindrome("madam"))
print(is_palindrome("Nurses Run"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
