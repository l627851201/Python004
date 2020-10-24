import pandas as pd

s1 = pd.Series(["15778","21227","15077"])
print(s1.to_list())
print(s1[1])

s2 = pd.Series(["15778","21227","15077"], index=["cai", 'liu', 'wang'])
print(s2)
print(s2[2])
print(s2['cai'])

print("="*20)
df1 = pd.DataFrame(['a','b','c','d'])
print(df1)
print(df1[0][1])

print("="*20)
df2 = pd.DataFrame(
    ['a', 'b', 'c', 'd'],
    [1, 2, 3, 4])
print(df2)

print("="*20)
df3 = pd.DataFrame([
    ['a', 'b', 'c', 'd'],
    [1, 2, 3, 4]
    ])
print(df3)
print(df3[2][1])
df3.columns = ['one', 'two', 'three', 'four']
print(df3)
df3.index = ['first', 'second']
print(df3)
print(df3['four']['first'])
print(df3.index)
print(df3.columns)
print(df3['four'].to_list())


