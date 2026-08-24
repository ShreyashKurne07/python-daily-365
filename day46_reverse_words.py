'''
Input:  "I love python"        → Output: "python love I"
Input:  "Chip War is good"     → Output: "good is War Chip"
Input:  "hello"                → Output: "hello"
'''
def reverse_order(words):

    word_list = words.split()
    word_list.reverse()

    print("Input:", words)
    print("Output:", " ".join(word_list))


reverse_order("I love python")
reverse_order("Chip War is good")
reverse_order("hello")
