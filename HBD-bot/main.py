import pandas as pd
import numpy as np
from datetime import datetime, timedelta

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


#список сотрудников, у которых ДР сегодня или в следующую неделю

filtered_data = df[(df['Дата рождения'].dt.strftime('%m-%d') >= today.strftime('%m-%d')) &
                   (df['Дата рождения'].dt.strftime('%m-%d') <= next_week.strftime('%m-%d'))]


print(filtered_data)

