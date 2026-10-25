'''
LeetCode 392: Is Subsequence

Problem statement: You are given two strings s and t. Return True if all the characters of s appear in t in the same order. 
They don’t need to be next to each other. Otherwise return False.

Expected output:
s = “abc”, t = “ahbgdc” -> True (a, then b, then c all appear in t in that order)
s = “axc”, t = “ahbgdc” -> False
s = “”, t = “abc” -> True
s = “abc”, t = “” -> False
'''

def isSubsequence(s, t):
    s_pointer = 0
    t_pointer = 0

    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1
    return s_pointer == len(s)

print(isSubsequence("abc","ahbgdc"))
print(isSubsequence("axc","ahbgdc"))
print(isSubsequence("","abc"))
print(isSubsequence("abc",""))
