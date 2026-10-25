import pandas as pd
data={
    "Name":["Aju","Biju","ciju","Diju","Eju","Fathima"],
    "Department":["CS","IT","CS","BCA","IT","CS"],
    "Sales":[25000,18000,32000,15000,28000,30000]
}
df=pd.DataFrame(data)
print("Original Dataset:")
print(df)
print("\nAscending Order:")
print(df.sort_values("Sales"))
print("\nDescending Order:")
print(df.sort_values("Sales",ascending=False))
group=df.groupby("Department")
print("\nDepartment-wise Average Sales:")
print(group["Sales"].mean())
print("\nDepartment-wise Employee Count:")
print(group["Name"].count())
