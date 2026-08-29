'''
Problem: Count how many vowels and consonants are in a string. Ignore spaces and numbers. 
Return a dictionary.
Input:  "hello world"   → Output: {'vowels': 3, 'consonants': 7}
Input:  "AEIOU"         → Output: {'vowels': 5, 'consonants': 0}
Input:  "abc 123"       → Output: {'vowels': 1, 'consonants': 2}

'''
def count_vowels_consonants(s):
        counts = {'vowels': 0, 'consonants': 0}
        vowels_list = "aeiou"

        for i in s:
                char = i.lower()
                if char.isalpha():

                        if char in vowels_list:
                                counts['vowels'] = counts['vowels'] + 1
                        else:
                                counts['consonants'] = counts['consonants'] + 1
        return counts
print(count_vowels_consonants("hello world"))
print(count_vowels_consonants("AEIOU"))
print(count_vowels_consonants("abc 123"))
