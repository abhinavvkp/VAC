import pandas as pd
data={
    "Name":["Anu","Binu","Cathy","David","Eva"],
    "Marks":[85,75,90,None,75],
    "Age":[20,21,None,20,21]
}
df=pd.DataFrame(data)
print("original dataset:")
print(df)
print("\nmissing values:")
print(df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print("\nafter filling missing values:")
print(df)
print("\nduplicate records:")
print(df[df.drop_duplicates()])
df=df.drop_duplicates()
print("\nafter removing duplicates:")
print(df)
df["Age"]=df["Age"].astype(int)
df["Name"]=df["Name"].astype(int)