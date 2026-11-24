numbers = [12, 7, 24, 9, 36, 15, 42]

'''
Print:
Even numbers
Odd numbers
Count of even and odd numbers

Even: [12, 24, 36, 42]
Odd: [7, 9, 15]
Even count: 4
Odd count: 3

'''

even = []
odd = []

for num in numbers:
        if num % 2 == 0:
                even.append(num)
        else:
                odd.append(num)

print("Even:",even)
print("Odd:",odd)
print("Even count:",len(even))
print("Odd count:",len(odd))

