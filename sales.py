import pandas as pd
df = pd.read_csv("sales.csv")
print("sales dataset")
print(df)
total_sales=df["sales"].sum()
print("\ntotal sales:",total_sales)
average_sales=df["sales"].mean()
print("average sales:",average_sales)
maximum_sales=df["sales"].max()
print("maximum sales:",maximum_sales)
minimum_sales=df["sales"].min()
print("minimum sales:",minimum_sales)
amount=30000
print("\ncustomers with sales greater than",amount,":")
result=df[df["sales"]>amount]
print("result")
print("\nsales data shorted by sales:")
shorted_df=df.sort_values(by="sales",ascending=False)
print("sorted_df")
