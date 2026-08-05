arr = [12, 45, 3, 67, 22, 8, 91, 34]


#Find max, min, sum — without max(), min(), sum(). One loop, track manually.
#Expected: Max: 91, Min: 3, Sum: 282

total_sum = 0
max_val = arr[0]
min_val = arr[0]

for i in arr:
	total_sum = total_sum + int(i)

	if (i > max_val):
		max_val = i
	if (i < min_val):
		min_val = i

print("Sum:",total_sum)
print("Maximum VALUE:",max_val)
print("Minimum Value:",min_val)
