#is_even(n) — takes a number, returns True if even, False if odd
#count_vowels(word) — takes a string, returns how many vowels (a,e,i,o,u) it has
#find_max(numbers) — takes a list, returns the biggest number (no max())

#print(is_even(10))
#print(is_even(7))
#print(count_vowels("Maharashtra"))
#print(find_max([12, 45, 3, 67, 22]))



def is_even(n):
	if (n % 2 == 0):
		return True

	else:
		return False





def find_max(list1):
	max_no = list1[0]
	for i in list1:
		if (i > max_no):
			max_no = i
	return max_no

def count_vowels(word):
	vowels = "aeiouAEIOU"
	count = 0
	for i in word:
		if i in vowels:
			count += 1
	return count


print(is_even(10))
print(is_even(7))
print(find_max([12,45,3,67,22]))
print(count_vowels("Maharashtra"))

