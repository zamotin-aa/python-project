import pandas as pd
import numpy as np

df = pd.read_excel("C:\\Users\\PC\\Desktop\\NEW2_PY\\IFT_emp.xlsx", sheet_name='TDSheet')

#поменял значения на datetime
df['Дата рождения'] = pd.to_datetime(df['Дата рождения'], dayfirst=True)
df['Дата увольнения'] = pd.to_datetime(df['Испытательный срок'], dayfirst=True)

#удалил ненужные столбцы
df.drop(['Подразделение', 'Организация', 'Табельный номер','Должность', 'Испытательный срок' ], axis= 1 , inplace= True )


print(df)
