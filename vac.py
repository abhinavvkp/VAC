import pandas as pd
df=pd.DataFrame({
    'Performance':['Low','High','Medium','High']
    })
df['Performance_Encoded']=df['Performance'].map({
    'Low':0,
    'Medium':1,
    'High':2
})
print(df)