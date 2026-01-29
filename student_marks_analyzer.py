students=[
    {"name":"Hari","marks":["78","85","35"]},
    {"name":"Keerthi","marks":["98","78","65"]},
    {"name":"Kishore","marks":["99","90","45"]},
    {"name":"Anand","marks":["98","98","97"]}
]
students = [
    {
        "name": s["name"],
        "marks": [int(m) for m in s["marks"]]
    }
    for s in students
]
averages=[
    {
        "name":s["name"],
        "average":sum(s["marks"])/len(s["marks"])
        }
    for s in students
]
passed_students = [s for s in averages if s["average"]>=50]
failed_students = [s for s in averages if s["average"]<50]
top_scorers = [s for s in averages if s["average"]>=85]
graded_students = [
    {
        "name":s["name"],
        "grade":"A" if s["average"]>=85 else
            "B" if s["average"]>=70 else
            "C" if s["average"]>=50 else
            "F"
    }
    for s in averages
]
print("Averages:",averages)
print("Passed Students:", passed_students)
print("Failed Students:",failed_students)
print("Top Scores:",top_scorers)
print("Grades:",graded_students)
