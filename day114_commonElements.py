list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80, 100]

'''
Print:
Common elements
Elements only in list1
Elements only in list2

Common: [20, 40]
Only list1: [10, 30, 50]
Only list2: [60, 80, 100]

'''

common = []
only1 = []
only2 = []

for num in list1:
        if num in list2:
                common.append(num)
        else:
                only1.append(num)

for num in list2:
        if num not in list1:
                only2.append(num)

print("Common:",common)
print("Only list1:",only1)
print("Only list2:",only2)
