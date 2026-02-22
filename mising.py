import pandas as pd
data={
    "Customer":["Hari","Ravi","Anu","Kiran","Divya"],
    "Weight":[10,8,None,12,8],
    "Wastage":[1,None,0.5,1.2,None],
    "Gold_rate":[6000,None,6100,6050,None],
    "Making_Charges":[800,400,None,600,450]
    }
df=pd.DataFrame(data)
print("Given data")
print(df)
print("\nMissing Values Count:")
print(df.isnull().sum())
df["Weight"]=df["Weight"].fillna(df["Weight"].mean())
df["Wastage"]=df["Wastage"].fillna(0.5)
df["Gold_rate"]=df["Gold_rate"].ffill()
df["Making_Charges"]=df["Making_Charges"].fillna(200)
df["Final_price"]=((df["Weight"]+df["Wastage"])*df["Gold_rate"])+df["Making_Charges"]
print("\nCLEANED DATA")
print(df)
top_customer=df.loc[df["Final_price"].idxmax()]
print(top_customer)
average_sale=df["Final_price"].mean()
print("\nAverage Sale value:",average_sale)
total_sales=df["Final_price"].sum()
print("Total Sales:",total_sales)

