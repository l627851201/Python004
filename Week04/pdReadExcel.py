import pandas as pd
import os

curr_path = os.path.abspath(os.path.dirname(__file__))
excels_path = os.path.join(curr_path, '1.xlsx')
excels1 = pd.read_excel(excels_path)
print(excels1)

excels2 = pd.read_excel(excels_path, sheet_name=0)
print(excels2)
print(excels2.head(2))
print(excels2.shape)
print(excels2.info())
print("="*20)

print(excels2.describe())



