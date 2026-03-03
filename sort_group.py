import pandas as pd
data={
    "Customer":["Ravi","Hari","Kishore","Keerthi","Sri"],
    "City":["Chennai","Chennai","Villupuram","Villupuram","Chennai"],
    "Weight":[8,4,40,80,4],
    "GoldRate":[16000,16500,15000,16000,16200]
    }
df=pd.DataFrame(data)
df["Sales"]=df["Weight"]*df["GoldRate"]
print("-----Full Data-----")
print(df)
print("\n----Highest Sales First-----")
var=df.sort_values("Sales",ascending=False)
print(var)
print("\n-----Lowest Gold Rate-----")
val=df.sort_values("GoldRate")
print(val)
print("\n-----Total Sales by City-----")
citysal=df.groupby("City")["Sales"].sum()
print(citysal)
print("\n-----Average Gold Rate by city-----")
avgrat=df.groupby("City")["GoldRate"].mean()
print(avgrat)
topcus=df.loc[df["Sales"].idxmax()]
print("\n-----Top Customer Details-----")
print(topcus)
