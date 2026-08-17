sentence = "the quick brown fox jumps over the lazy dog the fox runs"

'''
How many times each word appears.
The most repeated word and its count.
How many words appear only once.
All words that appear more than once, as a list.

Word counts: {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1, 'runs': 1}
Most repeated: the (3)
Words appearing once: 7
Repeated words: ['the', 'fox']

The Rules

Case-insensitive: Counting must be case-insensitive → "The" and "the" are the same word.
Clean Punctuation: Punctuation must not stick to words → "cricket." and "cricket" are the same word.
Tie-breaker: If two words tie for highest count, print the one that appeared first in the sentence.
'''
new = sentence.lower()
print(new)

sentence1 = []
sentence1 = new.replace(",","")
sentence1 = sentence1.replace(".","")
sentence1 = sentence1.split()

print(sentence1)

word_counts = {}


for i in sentence1:

	if i in word_counts:
		word_counts[i] += 1
	else:
		word_counts[i] = 1

print("Word counts:",word_counts)

sentence2 = word_counts.items()

most_repeated = ''
max_count = 0

appeared_once = 0

one_count = 1
repeated_word = []
for word,count in sentence2:

	if count > max_count:
		max_count = count
		most_repeated = word

	if count == 1:
		appeared_once += 1
	if count > 1:
		repeated_word.append(word)
print("Most repeated:",most_repeated,"("+ str(max_count)+")")
print("Words appearing once: ",appeared_once)
print("Repeated Words:",repeated_word)
