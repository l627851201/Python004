import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df2 = pd.DataFrame(sales)
print(df2)

print('**'*20)
group=['x','y','z']
data=pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
    })
print(data)

print('**'*20)
print(data.groupby('group').agg('mean'))
print(data.groupby('group').mean().to_dict())
print(data.groupby('group').transform('mean'))


# 数据透视表
df3 = pd.pivot_table(data, 
               values='salary', 
               columns='group', 
               index='age', 
               aggfunc='count', 
               margins=True  
            ).reset_index()
print(df3)


# 各类型产品的销售数量和销售总额
# print('**'*20)
# print(df2.groupby('type').aggregate( {'type':'count' , 'Feb':'sum' }))

# print('**'*20)
# print(df2.groupby('type').groups)

# print('**'*20)
# print(df2.groupby('type').count())
# print(df2.groupby('type').sum())



# print('**'*20)
# i = 0
# for a,b in df2.groupby('type'):
#     i += 1
#     print("i = {}".format(i))
#     print(a)
#     print(b)

# print('**'*20)
# i = 0
# for b in df2.groupby('type'):
#     i += 1
#     print("i = {}".format(i))
#     print(b)