import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Пример данных
data = {
    'Price': [10, 20, 30, 40, 50],
    'Advertising': [100, 200, 300, 400, 500],
    'Sales': [200, 250, 300, 350, 400]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Определяем независимые переменные (features) и зависимую переменную (target)
X = df[['Price', 'Advertising']]
y = df['Sales']

# Разделяем данные на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Создаем модель линейной регрессии
model = LinearRegression()

# Обучаем модель
model.fit(X_train, y_train)

# Делаем предсказания
y_pred = model.predict(X_test)

# Оцениваем модель
print('Коэффициенты:', model.coef_)
print('Свободный член:', model.intercept_)
print('Среднеквадратичная ошибка:', mean_squared_error(y_test, y_pred))
print('Коэффициент детерминации (R^2):', r2_score(y_test, y_pred))

# Пример предсказания для новых данных
new_data = pd.DataFrame({
    'Price': [25],
    'Advertising': [250]
})

predicted_sales = model.predict(new_data)
print('Предсказанные продажи для новых данных:', predicted_sales)


