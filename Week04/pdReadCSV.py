import pandas as pd
import os

current_path = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(current_path, 'book_utf8.csv')
print(csv_path)

df1 = pd.read_csv(csv_path)
# print(df1)

print("*"*30)
print(df1['还行'])