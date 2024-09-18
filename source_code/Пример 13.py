import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Сбор и разметка данных/HW/diploma/test.csv')

# Проверка названий столбцов
print("Названия столбцов в DataFrame:")
print(df.columns)

# Проверка наличия нужных столбцов
if 'GrLivArea' in df.columns:
    # Выбираем только столбец 'GrLivArea' для анализа и убираем пропущенные значения
    data = df[['GrLivArea']].dropna()

    # Поскольку у нас нет столбца 'SalePrice', мы используем 'GrLivArea' для прогнозирования
    # Это просто пример, и вы можете изменить модель и данные в зависимости от вашего анализа
    model = ARIMA(data['GrLivArea'], order=(5, 1, 0))
    model_fit = model.fit()

    # Прогнозирование на следующие 10 периодов
    forecast = model_fit.forecast(steps=10)

    # Визуализация фактических данных и прогноза
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['GrLivArea'], label='Фактические данные')
    plt.plot(range(len(data), len(data) + 10), forecast, label='Прогноз', color='red')
    plt.legend()
    plt.title('Визуализация прогноза временного ряда')
    plt.xlabel('Индекс')
    plt.ylabel('Жилая площадь (GrLivArea)')
    plt.show()
else:
    print("Столбец 'GrLivArea' отсутствует в DataFrame.")



