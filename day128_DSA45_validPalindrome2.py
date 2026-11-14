'''
LeetCode 680: Valid Palindrome II

Problem statement: You are given a string. Return True if it is a palindrome, or can become one by deleting at most one character. Otherwise return False. Don’t build new reversed strings with [::-1]; use two pointers.

Expected output:
“aba” -> True (already a palindrome, so nothing needs to be deleted)
“abca” -> True
“abc” -> False
“a” -> True
'''
def checkPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def validPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            skip_left = checkPalindrome(s, left + 1, right)
            skip_right = checkPalindrome(s, left, right - 1)

            return skip_left or skip_right
    return True

print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abc"))
print(validPalindrome("a"))
