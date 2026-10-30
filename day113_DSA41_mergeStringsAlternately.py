'''
LeetCode 1768: Merge Strings Alternately

Problem statement: You are given two strings word1 and word2. Build a new string by taking letters alternately, starting with word1. If one string is longer, add its remaining letters at the end. Return the new string.

Expected output:
“abc”, “pqr” -> “apbqcr” (a from word1, p from word2, b, q, c, r)
“ab”, “pqrs” -> “apbqrs”
“abcd”, “pq” -> “apbqcd”
“x”, “yz” -> “xyz”'''

def mergeStringsAlternately(word1,word2):
    result = []
    pointer1 = 0
    pointer2 = 0

    while pointer1<len(word1) and pointer2 < len(word2):
        result.append(word1[pointer1])
        result.append(word2[pointer2])
        pointer1 += 1
        pointer2 += 1
    while pointer1 < len(word1):
        result.append(word1[pointer1])
        pointer1 += 1

    while pointer2 < len(word2):
        result.append(word2[pointer2])
        pointer2 += 1
    return "".join(result)

print(mergeStringsAlternately("abc","pqr"))
print(mergeStringsAlternately("ab","pqrs"))
print(mergeStringsAlternately("abcd","pq"))
print(mergeStringsAlternately("x","yz"))

