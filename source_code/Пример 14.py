import pandas as pd

# Пример данных о компании и конкурентах
data = {
    'Company': ['Company A', 'Company B', 'Company C'],
    'Revenue': [1000000, 500000, 1500000],
    'Market_Share': [0.2, 0.1, 0.3],
    'price': [100, 95, 110],
    'service_quality': [8, 7, 6]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Нормализация данных  
df['Normalized_Revenue'] = df['Revenue'] / df['Revenue'].max()
df['Normalized_Market_Share'] = df['Market_Share'] / df['Market_Share'].max()
df['Normalized_Price'] = df['price'] / df['price'].max()
df['Normalized_Service_Quality'] = df['service_quality'] / df['service_quality'].max()

# Вычисление индекса конкурентоспособности
# Пример формулы: индекс = нормализованная выручка * 
# нормализованная рыночная доля * (1 - нормализованная цена) * нормализованное качество сервиса
df['Competitiveness_Index'] = (
    df['Normalized_Revenue'] * 
    df['Normalized_Market_Share'] * 
    (1 - df['Normalized_Price']) * 
    df['Normalized_Service_Quality']
)

print(df[['Company', 'Normalized_Revenue', 'Competitiveness_Index']])


