import pandas as pd
data={
    "Name":["Aju","Biju","ciju","Diju","Eju"],
    "Department":["CS","IT","CS","BCA","IT"],
    "Sales":[25000,18000,32000,15000,28000]
}
df=pd.DataFrame(data)
print("Dataset:")
print(df)
print("\nName and Sales Columns:")
print(df[["Name","Sales"]])
print("\nRow using loc:")
print(df.loc[2])
print("\nRow using iloc:")
print(df.iloc[2])
print("\nSales greater than 200000:")
print(df[df["Sales"]>20000])
print("\nIT Department:")
print(df.query("Department=='IT'"))
amount=25000
print("\nSales greater than",amount)
print(df[df["Sales"]>amount])
