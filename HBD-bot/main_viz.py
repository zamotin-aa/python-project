import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

today = datetime.now().date()
next_week = today + timedelta(days=7)

df = pd.read_excel("C:\\Users\\PC\\Desktop\\Учебное2023\\python-project\\HBD-bot\\IFT_emp.xlsx", sheet_name='TDSheet')

#поменял значения на datetime
df['Дата рождения'] = pd.to_datetime(df['Дата рождения'], dayfirst=True)
df['Дата приема'] = pd.to_datetime(df['Дата приема'], dayfirst=True)
df['Дата увольнения'] = pd.to_datetime(df['Испытательный срок'], dayfirst=True)

#оставил только тех, кто еще работает (дата увольнения пустая)      
df = df[df['Дата увольнения'].isnull()]

#удалил ненужные столбцы
df.drop(['Подразделение', 'Организация', 'Табельный номер', 
         'Дата увольнения', 'Испытательный срок', 'Должность',], axis= 1 , inplace= True )

#выделил из даты день и месяц
df['day'] = df['Дата рождения'].dt.day
df['month'] = df['Дата рождения'].dt.month

#отсортировал
df = df.sort_values(['month', 'day'])

#выделил полных лет
df['Сегодня'] = today
df['Сегодня'] = pd.to_datetime(df['Сегодня'], dayfirst=True)
df['Полных лет'] = (( df['Сегодня'] - df['Дата рождения'] ) / np.timedelta64(1, 'Y')).apply(np.floor)  

#удалил ненужные столбцы
df.drop(['Сегодня', 'day', 'month'], axis= 1 , inplace= True )
df = df.drop_duplicates(subset=['Сотрудник'])
df = df.reset_index(drop=True)


plt.figure()
plt.hist(df['Полных лет'])
plt.xlabel("Возраст")
plt.ylabel("Количество сотрудников")
plt.title('Распределение сотрудников по возрастным группам')
plt.show()
