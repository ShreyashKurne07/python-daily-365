'''
Day 61: Find Words Longer Than Target
Problem statement: Given a list of words and a number n, return a new list of all words that are strictly longer than n characters.
Input: ["apple", "bat", "computer"], n: 4 → Output: ["apple", "computer"]
'''

def filter_long_words(words, n):

        result = []
        for word in words:
                if len(word) > n:
                        result.append(word)
        return result

print(filter_long_words(["apple", "bat", "computer"], 4))
print(filter_long_words(["a", "ab", "abc"], 5))
