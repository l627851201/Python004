import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=12)
print(dates)
df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))
print(df)