numbers = [12, 45, 23, 67, 34, 67]

'''
Print:
All numbers
Largest number
Second largest number (without sort() or max())

Numbers: [12, 45, 23, 67, 34, 67]
Largest: 67
Second largest: 45

'''

print("Numbers:",numbers)

largest = 0
second_largest = 0

for num in numbers:
        if num > largest:
                second_largest = largest
                largest = num

        elif num > second_largest and num != largest:
                second_largest = num

print("Largest:",largest)
print("Second largest:",second_largest)
