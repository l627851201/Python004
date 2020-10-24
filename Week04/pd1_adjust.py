import pandas as pd
import numpy as np

# 行列调整
df = pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 

# # 查询指定列
# print(df[['A','C']])

# # 所有列表
# print(df.iloc[:])
# print('='*30)
# # 第1列，第3列
# print(df.iloc[:, [0,2]])

# # 行选择
# print('='*30)
# print(df)
# print('='*30)
# print(df.loc[[0,2]])
# print(df.loc[0:2])

# 比较
# print('='*30)
# print(df)
# print('='*30)
# print(df[ (df['A']<5) & (df['C']<4)])

# # 数值替换
# print('='*30)
# print(df)
# print('='*30)
# print(df['C'].replace(4, 40))

# # 数值替换
# print('='*30)
# print(df)
# print('='*30)
# print(df.replace(np.NaN, 0))

# # 数值替换
# print('='*30)
# print(df)
# print('='*30)
# print(df.replace([4,5,8], 666))

# # 数值替换
# print('='*30)
# print(df)
# print('='*30)
# print(df.replace({4:44, 5:55, 8:88}))

# # 排序
# # 按列，倒序排序
# print('='*30)
# print(df)
# print('='*30)
# print(df.sort_values(by = ['A'], ascending = False ))

# # 按列，倒序排序, TODO 待确定
# print('='*30)
# print(df)
# print('='*30)
# # print(df.sort_values(by = ['A', 'C'], ascending = [True, False]))
# print(df.sort_values ( by = ['A','C'] ,ascending = [True,False]))

# 删除
# # 删除列
# print('='*30)
# print(df)
# print('='*30)
# print(df.drop('A', axis=1))

# # 删除列
# print('='*30)
# print(df)
# print('='*30)
# print(df.drop(3, axis=0))

# 删除特定行, TODO 待确定
# print('='*30)
# print(df)
# print('='*30)
# print(df[ df['A'] < 4]])
# print(df.drop(df['A'] < 4))

# # 行列互换
# print('='*30)
# print(df)
# print('='*30)
# print(df.T)
# print('='*30)
# print(df.T.T)

# 索引重塑
df4 = pd.DataFrame([
                     ['a', 'b', 'c'], 
                     ['d', 'e', 'f']
                    ],
                    columns= ['one', 'two', 'three'],
                    index = ['first', 'second']
                   )       
print(df4)
print('='*30)
print(df4.stack())
print('='*30)
print(df4.unstack())
print('='*30) 
print(df4.stack().reset_index())





