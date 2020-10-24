import pandas as pd
import numpy as np

x = pd.Series([1, 2, np.nan, 4, 5, np.nan, 7, 8, np.nan])
print(x)
print(x.hasnans)

# 填充缺失值
x1 = x.fillna(value = x.mean())
print(x1)
print("*"*30)
print(x)

df3=pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 
                 
print(df3)
print("*"*30)
print(df3.isnull().sum())

# 用上一行
print(df3.ffill())
print("*"*30)
print(df3)

# 用前一列填充
print(df3.ffill(axis=1))
print("*"*30)
print(df3)

# 缺失值删除
print("*"*30)
print(df3.info())
print("*"*30)
print(df3.dropna())

print("*"*30)
print(df3.fillna('无'))

print("*"*30)
print(df3)
print("*"*30)
print(df3.drop_duplicates())


