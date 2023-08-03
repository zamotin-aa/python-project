import pandas as pd
import numpy as np

# Конструктор класса Series выглядит следующим образом:
# Series(data=None, index=None, dtype=None, name=None, copy=False,
# fastpath=False)

# Ниже перечислены способы объявления серии

# s1 = pd.Series([1, 2, 3, 4, 5])
# print(s1)

# s2 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
# print(s2)

# ndarr = np.array([1, 2, 3, 4, 5])
# type(ndarr)
# s3 = pd.Series(ndarr, ['a', 'b', 'c', 'd', 'e'])
# print(s3)

# d = {'a':1, 'b':2, 'c':3}
# s4 = pd.Series(d)
# print(s4)

# a = 7
# s5 = pd.Series(a, ['a', 'b', 'c'])
# print(s5)

#работать с фреймами

s6 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
#print(s6[2]) # s6['d']

#срез print(s6[:2]) 
#диапазон s6[s6 <= 3]

s7 = pd.Series([10, 20, 30, 40, 50], ['a', 'b', 'c', 'd', 'e'])

#можно складывать и умножать
print (s6+s7*40)





