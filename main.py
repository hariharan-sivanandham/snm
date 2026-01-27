from student_data import students
from result_analysis import analyze_students
analyze_students(students)

import student_utils

marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

total = student_utils.calculate_total(marks)
average = student_utils.calculate_average(marks)
grade = student_utils.calculate_grade(average)

print("Total:", total)
print("Average:", average)
print("Grade:", grade)
