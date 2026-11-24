marks = {"Amit": 78, "Rahul": 32, "Neha": 85, "Riya": 28, "Om": 65}

'''
Print:
Passed students (marks >= 40)
Failed students
Average marks

Passed: ['Amit', 'Neha', 'Om']
Failed: ['Rahul', 'Riya']
Average: 57.6

'''

passed = []
failed = []
total = 0

for name,score in marks.items():
        total += score

        if score >= 40:
                passed.append(name)
        else:
                failed.append(name)

average = total / len(marks)

print("Passed:",passed)
print("Failed:",failed)
print("Average:",average)

