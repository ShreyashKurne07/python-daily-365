'''
Python problem: Given a dictionary of student names and their marks list, return a new dictionary of name → average marks (rounded to 2 decimals).

Input:  {"Amit": [80,90,70], "Riya": [60,65]}
Output: {'Amit': 80.0, 'Riya': 62.5}
'''
def get_averages(student_marks):

        result = {}
        for name in student_marks:
                marks = student_marks[name]
                total = 0
                for i in marks:
                        total = total + i
                average = total / len(marks)
                result[name] = round(average, 2)
        return result
print(get_averages({"Amit": [80, 90, 70], "Riya": [60, 65]}))
