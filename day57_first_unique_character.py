'''
Day 57: First Unique Character
Problem statement: Given a string, find the first non-repeating character and return it. If it doesn't exist, return "" (empty string).
Input: "leetcode" → Output: "l"
'''

def first_unique(s):

        counts = {}
        for i in s:
                if i in counts:
                        counts[i] = counts[i] + 1
                else:
                        counts[i] = 1
        for i in s:
                if counts[i] == 1:
                        return i
        return ""

print(first_unique("leetcode"))
print(first_unique("aabb"))
