import pandas as pd
import numpy as np

# Конструктор класса DataFrame выглядит так:
# DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

# элементы — это структуры Series
# d = {'price':pd.Series([1, 2, 3], index=['v1', 'v2', 'v3']),'count':pd.Series([10, 12, 7], index=['v1', 'v2', 'v3'])}
# df1 = pd.DataFrame(d)
# print(df1)
# print(df1.index)
# print(df1.columns)

# Построим аналогичный словарь, но на элементах ndarray
# d2 = {'price':np.array([1, 2, 3]), 'count': np.array([10, 12, 7])}
# df2 = pd.DataFrame(d2, index=['v1', 'v2', 'v3'])
# print(df2)
# print(df2.index)
# print(df2.columns)

# Создание DataFrame из списка словарей
# d3 = [{'price': 3, 'count':8}, {'price': 4, 'count': 11}]
# df3 = pd.DataFrame(d3)
# print(df3.info())

# Создание DataFrame из двумерного массива
# nda1 = np.array([[1, 2, 3], [10, 20, 30]])
# df4 = pd.DataFrame(nda1)
# print(df4)




