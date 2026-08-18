# Problem Statement: Given a sentence, count word frequencies using a dictionary. 
# Identify the most repeated word (first occurrence wins in a tie), 
# a list of words that appeared only once, and a list of words that repeated.
#
# Expected Output for "cat dog cat dog bird":
# ('cat', ['bird'], ['cat', 'dog'])

def analyze_sentence(sentence):
    word_counts = {}
    for word in sentence.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    most_repeated = ""
    max_count = 0
    appeared_once = []
    repeated_words = []

    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_repeated = word

        if count == 1:
            appeared_once.append(word)
        else:
            repeated_words.append(word)

    return most_repeated, appeared_once, repeated_words

print(analyze_sentence("cat dog cat dog bird"))
