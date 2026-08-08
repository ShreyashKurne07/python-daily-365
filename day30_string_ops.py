sentence = "Pune is the IT hub of Maharashtra and my home city"

#Total number of words
#Total number of characters (including spaces)
#The longest word in the sentence
#How many words start with a capital letter
#The sentence in reverse word order (not reverse letters) — e.g. "city home my..."

count = 0
char_count = 0
cap_letter = 0
rev = 0

words = sentence.split()
print(words)

for i in words:
	count += 1

for i in sentence:
	char_count += 1

print("Word Count:",count)
print(char_count)


long_word = words[0]
for i in words:
	if (len(i) > len(long_word)):
		long_word = i

print(long_word)

for i in words:
	if (i[0].isupper()):
		cap_letter += 1

print(cap_letter)


words.reverse()

print(" ".join(words))
