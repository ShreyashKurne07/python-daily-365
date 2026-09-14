'''
Leetcode 125
Given a string s, return True if it is a palindrome after converting all uppercase to lowercase and removing all non-alphanumeric characters (keep only letters and numbers). Otherwise return False.
Expected output:


Input:  "A man, a plan, a canal: Panama"
Output: True

Input:  "race a car"
Output: False

Input:  " "
Output: True   (empty after cleaning → counts as palindrome)
'''

def is_palindrome(s):
        cleaned_s = ""

        for i in s:
                if i.isalnum():
                        cleaned_s = cleaned_s + i.lower()
        reversed_s = ""
        for i in cleaned_s:
                reversed_s = i + reversed_s
        if cleaned_s == reversed_s:
                return True
        else:
                return False

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))
