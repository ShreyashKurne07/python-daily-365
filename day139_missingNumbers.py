numbers = [1, 2, 4, 6, 7, 10]

'''
Print:
All numbers
Missing numbers between 1 and 10
Total missing numbers

Numbers: [1, 2, 4, 6, 7, 10]
Missing: [3, 5, 8, 9]
Total missing: 4

'''

missing = []

for num in range(1,11):
        if num not in numbers:
                missing.append(num)

print("Numbers:",numbers)
print("Missing:",missing)
print("Total missing:",len(missing))
