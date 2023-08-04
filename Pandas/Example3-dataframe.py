import pandas as pd
import numpy as np

d = {'price':np.array([1, 2, 3]), 'count': np.array([10, 20, 30])}
df = pd.DataFrame(d, index=['a', 'b', 'c'])

# Операция: выбор столбца:
# df['count']

# Операция: выбрать столбец - работает только так
# print(df['count'])
# Операция: выбрать столбец - не работает
# df['count']

# Операция: выбор строки по метке:
# print(df.loc['a'])

# Операция: выбор строки по индексу:
# print(df.iloc[1])

# # Операция: срез по строкам:
# print(df[0:2])

# Операция: выбор строк, отвечающих условию:
# print(df[df['count'] >= 20])

# Или так
df2 = df[df['count'] >= 20]
print(df2)
