'''
LeetCode 290: Word Pattern

Problem statement: You are given a pattern string of letters and a string s of words separated by single spaces. 
Return True if s follows the pattern: each letter maps to exactly one word, and no two letters map to the same word. 
This is LC 205 with words instead of characters. Watch out for the case where the number of words doesn't match the number of 
letters.

Expected output:
"abba", "dog cat cat dog" -> True (a→dog and b→cat, and the mapping stays the same every time)
"abba", "dog cat cat fish" -> False
"aaaa", "dog cat cat dog" -> False
"abba", "dog dog dog dog" -> False
'''

def wordPattern(s, t):
    words = t.split()

    if len(s) !=len(words):
        return False
    s_t = {}
    t_s = {}

    for i in range(len(s)):
        char_s = s[i]
        word_t = words[i]

        if char_s in s_t and s_t[char_s] != word_t:
            return False

        if word_t in t_s and t_s[word_t] != char_s:
            return False

        s_t[char_s] = word_t
        t_s[word_t] = char_s
    return True

print(wordPattern("abba",  "dog cat cat dog"))
print(wordPattern("abba",  "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("abba",  "dog dog dog dog"))
