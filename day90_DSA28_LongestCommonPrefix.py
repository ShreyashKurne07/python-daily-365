'''LeetCode 14: Longest Common Prefix

Problem statement: You are given a list of strings. Return the longest starting part that all the strings share. If they share 
nothing at the start, return an empty string "".

Expected output:
["flower", "flow", "flight"] -> "fl" (all three start with "fl", but the third letter differs: o, o, i)
["dog", "racecar", "car"] -> ""
["interview", "internet", "interval"] -> "inter"
["a"] -> "a"
'''

def longestCommonPrefix(list1):
    prefix = list1[0]

    for i in list1:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
        if prefix == "":
            return ""
    return prefix
print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["interview", "internet", "interval"]))

