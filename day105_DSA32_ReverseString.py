'''
Problem 1: LeetCode 344: Reverse String
Problem statement: You are given a list of 
characters. Reverse it in place, meaning you 
change the same list and return nothing. 
Use O(1) extra space. Don’t use reverse(), [::-1]
, or a new list.
Expected output:

[“h”,”e”,”l”,”l”,”o”] -> [“o”,”l”,”l”,”e”,”h”] 
(the first and last swap places, then the second 
and second-last, and so on)

[“H”,”a”,”n”,”n”,”a”,”h”] -> [“h”,”a”,”n”,”n”,”a”,”H”]

[“a”] -> [“a”]

[“a”,”b”] -> [“b”,”a”]
'''

def reverseString(s):

    left = 0
    right = len(s) - 1

    while left < right:

        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

word = ["h", "e", "l", "l", "o"]
reverseString(word)
print(word)
