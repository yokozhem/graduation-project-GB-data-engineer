import pandas as pd

# Загрузка данных из CSV-файла
data = pd.read_csv('diploma/test.csv')

# Вывод первых пяти строк 
print(data.head())

# Проверка типа данных в каждом столбце
print(data.dtypes)

# Преобразование всех столбцов, которые должны содержать числовые данные, в числовой формат
data = data.apply(pd.to_numeric, errors='ignore')

# Вычисление среднего значения для каждого столбца (только для числовых данных)
mean_values = data.mean(numeric_only=True)

# Вычисление медианы для каждого столбца (только для числовых данных)
median_values = data.median(numeric_only=True)

# Вычисление стандартного отклонения для каждого столбца (только для числовых данных)
std_values = data.std(numeric_only=True)

print('Средние значения:\n', mean_values)
print('Медианные значения:\n', median_values)
print('Стандартные отклонения:\n', std_values)


