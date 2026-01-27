from calculations import average
def analyze_students(students):
    for student in students:
        avg = average(student["marks"])
        print(student["name"],"-Average Marks:",avg)
