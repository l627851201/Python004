import pandas as pd
import numpy as np

group = ['x', 'y', 'z', 'a', 'b', 'c']
length = 15
data = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), length)],
    "id": np.random.randint(900, 1100, length),
    "age": np.random.randint(5, 70, length),
    "score": np.random.randint(1, 10, length)
})

# 作业要求：请将以下的 SQL 语句翻译成 pandas 语句：

# 1. SELECT * FROM data;
print("="*20)
print(data)
print("="*20)
print(data2)

# 2. SELECT * FROM data LIMIT 10;
print("="*20)
print(data.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print("="*20)
print(data.id)

# 4. SELECT COUNT(id) FROM data;
print("="*20)
print(data.id.count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print("="*20)
print(data[(data.id < 1000) & (data.age > 30) ])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print("="*20)
print(data.groupby('id').size())

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
data = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), length)],
    "id": np.random.randint(1, 10, length),
    "age": np.random.randint(5, 70, length),
    "score": np.random.randint(1, 10, length)
})

data2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), length)],
    "id": np.random.randint(1, 10, length),
    "age": np.random.randint(5, 70, length),
    "score": np.random.randint(1, 10, length)
})
print("="*20)
print(pd.merge(data, data2, left_on='id', right_on='id', how='inner'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print("="*20)
print(pd.concat([data, data2]))

# 9. DELETE FROM table1 WHERE id=10;
data = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(1, len(group), length)],
    "id": np.random.randint(1, 5, length),
    "age": np.random.randint(5, 70, length),
    "score": np.random.randint(1, 10, length)
})
print(data)

print("="*20)
# data_drop = data.drop(data['id'] == 1, axis=1)
data_drop = data.drop(data[data['id'] == 1].index)
print(data_drop)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print("="*20)
print(data.drop('id', axis = 1))