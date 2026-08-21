"""
Day 43: LeetCode 242 - Valid Anagram
Difficulty: Easy

Problem Statement:
Given two strings s and t, return True if t is an anagram of s, otherwise return False.
"""
def is_anagram(s, t):
        if len(s) != len(t):
                return False

        s_counts = {}
        t_counts = {}

        for i in s:
                if i in s_counts:
                        s_counts[i] = s_counts[i] + 1
                else:
                        s_counts[i] = 1

        for i in t:
                if i in t_counts:
                        t_counts[i] = t_counts[i] + 1
                else:
                        t_counts[i] = 1

        if s_counts == t_counts:
                return True
        else:
                return False


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("ab", "a"))
