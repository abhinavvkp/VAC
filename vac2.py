import pandas as pd
sales=pd.Series([12000,15000,18000,14000,20000])
print("Sales Series:")
print(sales)
data={
    "Name":["Anu","Binu","Cathy","David","Eva"],
    "Marks":[85,72,90,65,78],
    "Grade":["A","B","A+","C","B"]
}
df=pd.DataFrame(data)
print("\nStudent DataFrame:")
print(df)
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print("\nDataset Information:")
df.info()
print("\nStatistical Summery:")
print(df.describe())
