import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Загрузка данных временного ряда
data = pd.read_csv('WeeklyClosing.csv', index_col='Week', parse_dates=True)

# Применение модели ARIMA (p=5, d=1, q=0)
model = ARIMA(data, order=(5, 1, 0))
model_fit = model.fit()

# Прогнозирование на следующие 10 периодов
forecast = model_fit.forecast(steps=10)

# Визуализация прогноза
plt.figure(figsize=(10, 6))
plt.plot(data, label='Исторические данные')
plt.plot(forecast, label='Прогноз', color='red')
plt.legend()
plt.show()

