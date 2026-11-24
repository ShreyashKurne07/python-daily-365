word = "programming"

'''
Print:
Frequency of each character

Output:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

'''

frequency = {}

for ch in word:
        if ch in frequency:
                frequency[ch] += 1
        else:
                frequency[ch] = 1

print(frequency)
