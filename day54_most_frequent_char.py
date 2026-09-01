'''
Problem: Given a string, return the character that appears most often. On a tie, return the one that appeared first.


Input:  "programming"   → Output: 'r'
Input:  "aabb"          → Output: 'a'  (tie, 'a' came first)
Input:  "xyz"           → Output: 'x'
'''

def most_frequent(s):

        counts = {}

        for i in s:
                if i in counts:
                        counts[i] = counts[i] + 1
                else:
                        counts[i] = 1
        max_char = ""
        max_count = 0
        for i in counts:
                if counts[i] > max_count:
                        max_count = counts[i]
                        max_char = i
        return max_char
print(most_frequent("programming"))
print(most_frequent("aabb"))
print(most_frequent("xyz"))
