import pandas as pd
import numpy as np

group = ['x', 'y', 'z']
data1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), 10)],
    "salary": np.random.randint(5, 50, 10)
})

data2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), 10)],
    "salary": np.random.randint(5, 50, 10)
})

data3 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), 10)],
    "salary": np.random.randint(5, 50, 10)
})

print(data1)
print(data2)
print(data3)

# print("**"*20)
# print(pd.merge(data1, data2))

# 多对一
print("**"*20)
pd.merge(data3, data2, on='group')
