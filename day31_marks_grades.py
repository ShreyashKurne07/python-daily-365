marks = [78, 45, 92, 33, 66, 88, 51, 29]

#How many passed (35 and above)
#How many failed
#Highest mark and lowest mark
#Count of distinction (75 and above)
#Class average, rounded to 2 decimals

passed = 0
failed = 0
distinction = 0
total_sum = 0

max_mark = marks[0]
min_mark = marks[0]

for i in marks:
	if (i >= 35):
		passed += 1


	if (i <35):
		failed += 1

	if (i > max_mark):
		max_mark = i

	if (i < min_mark):
		min_mark = i

	if (i >= 75):
		distinction += 1

	total_sum = total_sum + i

average = total_sum / len(marks)

print("Passed:", passed)
print("Failed:", failed)
print("Highest:", max_mark)
print("Lowest:", min_mark)
print("Distinction:", distinction)
print("Average:", round(average, 2))

