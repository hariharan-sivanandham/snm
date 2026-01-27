students = []
n=int(input("Enter number of students:"))
for i in range(n):
    name =input(f"\nEnter name of student{i+1}:")
    marks=[]
    subjects=int(input("Enter number of subjects:"))
    for j in range(subjects):
        mark=int(input(f"Enter mark for subject{j+1}:"))
        marks.append(mark)
        students.append({
            "name":name,
            "marks":marks
            })
