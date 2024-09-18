import pandas as pd # для обработки и анализа данных
import numpy as np # библиотека  для работы с массивами
import matplotlib.pyplot as plt # модуль  для  построения графиков
import seaborn as sns # библиотека для визуализации данных, основаня для matplotlib
from sklearn.preprocessing import LabelEncoder  # для кодирования категориальных переменных
from scipy import stats # библиотека для научных и математических вычислений

# Установка  стиля  и цветной палитры для графиков
sns.set(style='whitegrid')
# Загрузка данных 
file_path = '/Users/pelmeshka/Documents/Обучение/Сбор и разметка данных/lessons/lesson_8/googleplaystore.csv'
df = pd.read_csv(file_path) #  читает первые пять строк

# Вывод датасета
print('Первые строки датасета')
print(df)


print("\n статистика: ")
print(df.describe())

print("\n Описательная статистика: ")
# print(df.stats())

#обработка отсутсвующих значений
#Всем пропущенным данным мы присволили значение

numeric_cols = df.select_dtypes(include=[np.number]) # выбор числовых колонок
df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean()) # замена пропущенных значений на среднее
print(df[numeric_cols.columns])

categorial_cols = df.select_dtypes(include= ['object']) #выбор категориальных колонок
df[categorial_cols.columns] = categorial_cols.fillna(categorial_cols.mode().iloc[0]) #замена пропущенных значений на моду
print(df[categorial_cols.columns])

#удаление дублирующих  строк
df.drop_duplicates(inplace= True)

# # гистограмма распределения рейтингов
# plt.figure(figsize= (10, 6))
# sns.histplot(df['Rating'], kde = True, color= 'skyblue') # построение  гистограммы  и кривой плотности рапределения
# plt.title("Distr of App rating")
# plt.show() # отображение  графика

# # распределение приложений по  категориям
# plt.figure(figsize= (12, 8))
# sns.countplot(y= 'Category', data= df,  order= df['Category'].value_counts().index, palette='viridis')
# plt.title("App Distr across Categories")
# plt.show() # отображение  графика

# #  распределение платных и бесплатных приложений
# plt.figure(figsize= (7, 5))
# sns.countplot(x="Type", data=df)
# plt.title("Free vs Paid")
# plt.show() # отображение  графика


# Boxplot для распределения рейтингов по категориям
plt.figure(figsize=(12, 8))
sns.boxplot(x='Rating', y='Category', data=df, palette='Set3')
plt.title("Boxplot распределения рейтингов по категориям")
plt.show()

# Тепловая карта корреляций
plt.figure(figsize=(10, 8))

# Выбираем только числовые колонки для вычисления корреляций
numeric_data = df.select_dtypes(include=[np.number])

# Вычисляем корреляционную матрицу
corr = numeric_data.corr()

# Создаем тепловую карту
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Тепловая карта корреляций")
plt.show()


# обнаружение и обработка выбросов
z_scores = np.abs(stats.zscore(df.select_dtypes(include= np.number))) # z оценка  для числовых переменных
df = df[(z_scores < 3).all(axis= 1)] # удаление строк с выбросами

# Стандартизация данных
df_standardised = df.copy() #копия датафрема

# Преобразование числовых колонок в DataFrame
numeric_data = df_standardised[numeric_cols.columns]
df_standardised[numeric_cols.columns] = (numeric_data - numeric_data.mean()) / numeric_data.std()


#Создание допстолбца
label_encoder = LabelEncoder()
df['Type_Encoded'] = label_encoder.fit_transform(df['Type']) #преобразование категориальной переменной в числовую

df = pd.get_dummies(df,columns= ["Content Rating"], prefix= 'ContentRating', drop_first= True)

#Создание сводной таблицы
pivot_table = df.pivot_table(index = 'category', columns = 'ContentRating_Teen', value = 'Rating', aggfunc = 'mean') 
print('/n сводная таблица:')
print(pivot_table)

output_file_path =  'clear_gapps.cav'
df.to_csv(output_file_path, index= False)



 