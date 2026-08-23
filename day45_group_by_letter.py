''' Given a list of words, group them into a dictionary by their first letter. The key is the
first letter (lowercase), and the value is a list of all words starting with that letter, in
the order they appeared.

Input:  ["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]
Output: {'a': ['apple', 'avocado', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

Input:  ["Dog", "deer", "Cat"]
Output: {'d': ['Dog', 'deer'], 'c': ['Cat']}
(key is lowercase, but the word itself keeps its original spelling)

Input:  []
Output: {}

'''

def group_by_first_letter(words):
	grouped_words = {}

	for i in words:
		first_letter = i[0].lower()

		if first_letter in grouped_words:
			grouped_words[first_letter].append(i)
		else:
			grouped_words[first_letter] = [i]
	return grouped_words

print(group_by_first_letter(["apple", "banana", "avocado", "cherry", "blueberry", "apricot"]))
print(group_by_first_letter(["Dog", "deer", "Cat"]))
print(group_by_first_letter([]))








