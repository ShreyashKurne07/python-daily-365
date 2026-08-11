'''Write three functions:

1.only_even(numbers) — takes a list, returns a new list with only even numbers
2.above_average(numbers) — takes a list, returns a new list with only numbers above the list's average

3.word_lengths(words) — takes a list of words, returns a new list of their lengths

print(only_even([12, 7, 4, 9, 20, 33, 6]))
print(above_average([10, 20, 30, 40, 50]))
print(word_lengths(["Pune", "Maharashtra", "IT", "hub"]))

[12, 4, 20, 6]
[40, 50]
[4, 11, 2, 3]
'''

def only_even(numbers):
	list1 = []
	for i in numbers:
		if (i % 2 == 0):
			list1.append(i)

	return list1
print(only_even([12, 7, 4, 9, 20, 33, 6]))

def above_average(numbers):
	list2 = []

	average = sum(numbers) / len(numbers)

	for i in numbers:
		if (i > average):
			list2.append(i)
	return list2
print(above_average([10,20,30,40,50]))

def word_lengths(words):
	list3 = []
	for i in words:
		list3.append(len(i))
	return list3
print(word_lengths(["Pune", "Maharashtra", "IT", "hub"]))

