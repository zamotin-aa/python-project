#Конспект по порядку проведения EDA
#Датасет взят с kaggle

#Импортирую нужные библиотеки
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import missingno

#Загрузка и предварительный просмотр просмотр файла (разделитель в csv - ',')
# df = pd.read_csv("C:\\Datasets\\Salary_Dataset_with_Extra_Features.csv", sep = ',')
df = pd.read_excel("C:\\Datasets\\Отчеты ERP\\Orders.xlsx", sheet_name='TDSheet')

# print(df.info())
# print(df.head())
# print(df.shape) #Вывести сколько строк, столбцов
# print(df.dtypes) #Вывести типы данных каждого столбца
#print(df.describe()) #Вывести сводную статистику числовых переменных в наборе данных, 
#включая количество, среднее значение, стандартное отклонение, минимальные и 
#максимальные значения для каждой переменной.


#Удалить дубликаты (если есть) 
#df = df.drop_duplicates()

#Посмотреть нулевые значения (если есть)
# метод .isnull() выдает логический массив, где пропуски обозначены как True
# метод .sum() по умолчанию суммирует эти True или единицы по столбцам (axis = 0)
# print(df.isnull().sum())

# Часть кода, релевантная для проверки пропущенных значений
# if len(df[df.isnull().any(axis=1)] != 0):
#     print("\nPreview of data with null values:\nxxxxxxxxxxxxx")
#     print(df[df.isnull().any(axis=1)].head(3))
#     missingno.matrix(df)
#     plt.show()
# Больше - хороший пример тут
# https://machinelearningmastery.ru/exploratory-data-analysis-eda-a-practical-guide-and-template-for-structured-data-abfbf3ee3bd9/

#Удалить ненужные столбцы
df.drop(['Договор.Дата поставки по договору', 'Договор.Идент. Код закупки', 'Договор.Идентификатор госконтракта', 
         'Направление деятельности', 'Объект', 'Согласован', 'Стадия заказа', 
         'Статус', 'Тип заказа', 'Тип рынка', 'Транспорт'], axis= 1 , inplace= True )

df = df.dropna(subset=['Сумма документа']) #удалил строки, к которых сумма заказа нулевая
#print(df['Этап заказа клиента'].info()) #посмореть инфо только по одному столбцу

# print(df['Этап заказа клиента'].value_counts()) #посмотреть уникальные значения по столбцу

#расставляем правильные типы данных

df[['Заказ клиента.Номер', 
    'Этап заказа клиента',
    'Клиент',
    'Договор',
    'Валюта',
    'Цена включает НДС',
    'Договор.ГОЗ 275ФЗ',
    'Договор.Ставка НДС',
    'Военная приемка (ВП)',
    'Специалист отдела продаж',
    'Менеджер'
    ]] = df[[   'Заказ клиента.Номер', 
                'Этап заказа клиента',
                'Клиент',
                'Договор',
                'Валюта',
                'Цена включает НДС',
                'Договор.ГОЗ 275ФЗ',
                'Договор.Ставка НДС',
                'Военная приемка (ВП)',
                'Специалист отдела продаж',
                'Менеджер']].astype('string')
    
df['Дата отгрузки'] = pd.to_datetime(df['Дата отгрузки'])

#фильтр по нужным типам заказов

#создадим список правильных типов (у нас два варианта списков)
order_types_actual = ['1_1 План (бюджет)','2. Согласование договора','3. Договор заключен']
order_types_fact = ['2. Согласование договора','3. Договор заключен', '4. Отгружено','5. Завершено']

#отфильтруем используя метод isin
df = df[df['Этап заказа клиента'].isin(order_types_fact)]

#доп.фильтр по этому году
df = df[(df['Дата отгрузки'] > "2023-01-01") & (df['Дата отгрузки'] < "2023-12-31")]

df.groupby(['Этап заказа клиента'])['Сумма документа'].sum().plot.barh(x="Этап заказа клиента", y = "Сумма документа")
plt.show()
# print(df.info())
# print(df.shape)