import pandas as pd
gold_rate=12000
data={
    "Customer":["Hari","keerthi"],
    "Gold weight":[8,16],
    "Making charge":[250,500],
}
df=pd.DataFrame(data)
df["Gold Price"]=df["Gold weight"]*gold_rate
df["total"]=df["Gold Price"]+df["Making charge"]
print(df)
