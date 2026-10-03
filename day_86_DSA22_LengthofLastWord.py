'''
Problem 2: LeetCode 58: Length of Last Word

Problem statement: You are given a string made of words and spaces. Return the length of the last word in the string. 
A word is a group of non-space characters. The string can have extra spaces at the start, between words, and at the end.

Expected output:
"Hello World" -> 5 (the last word is "World", which has 5 letters)
" fly me to the moon " -> 4
"luffy is still joyboy" -> 6
"a" -> 1'''
def lastWordCount(sentence):
    words = sentence.split()
    return len(words[-1])

print(lastWordCount("Hello World"))
print(lastWordCount("  fly me to the moon  "))
print(lastWordCount("luffy is still joyboy"))
print(lastWordCount("a"))
