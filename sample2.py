import pandas as pd

data = {
    "Name": ["Hari", "Priya", "Kumar"],
    "Math": [80, 96, 98],
    "Science": [76, 98, 80],
    "English": [98, 88, 87]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = df["Total"] / 3

def grade(p):
    if p >= 80:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)

print("\nFull Result:")
print(df)

topper = df.loc[df["Total"].idxmax()]
print("\nTopper Details:")
print(topper)

fail_students = df[df["Grade"] == "Fail"]
print("\nFail Students:")
print(fail_students)

class_average = df["Percentage"].mean()
print("\nClass Average Percentage:", class_average)
