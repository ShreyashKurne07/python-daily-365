'''
LeetCode 205: Isomorphic Strings

Problem statement: You are given two strings s and t of the same length. They are isomorphic if every character in s can be replaced to get t, where each character always maps to the same character, and no two different characters map to the same character. A character can map to itself. Return True or False.

Expected output:
“egg”, “add” -> True (e→a, g→d, and the mapping stays the same every time)
“foo”, “bar” -> False
“paper”, “title” -> True
“badc”, “baba” -> False'''

def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
            
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
