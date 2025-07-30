import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_path = r'C:\Users\khair\Downloads\amazon2.csv'
df = pd.read_csv(csv_path, encoding='ISO-8859-1', thousands='.')

print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe(include='all'))
print(df.isna())
print(df.isna().sum())
print(df['number'].replace(0, np.nan))

df2 = df.dropna(subset=['number'])
print(df2)
print(df2.describe(include='all'))

forest_fire_per_month = df2.groupby('month')['number'].sum()
print(forest_fire_per_month)

months_unique = list(df['month'].unique())
print(months_unique)
forest_fire_per_month = forest_fire_per_month.reindex(months_unique, axis=0)
print(forest_fire_per_month)

forest_fire_per_month = forest_fire_per_month.reset_index(level=0)
print(forest_fire_per_month.head())

month_translation = {
    'Janeiro': 'January',
    'Fevereiro': 'February',
    'Março': 'March',
    'Abril': 'April',
    'Maio': 'May',
    'Junho': 'June',
    'Julho': 'July',
    'Agosto': 'August',
    'Setembro': 'September',
    'Outubro': 'October',
    'Novembro': 'November',
    'Dezembro': 'December'
}

forest_fire_per_month['month'] = forest_fire_per_month['month'].map(month_translation)
forest_fire_per_month = forest_fire_per_month.dropna(subset=['month'])  # 🧼 Drop bad rows


forest_fire_per_month['number'] = pd.to_numeric(forest_fire_per_month['number'], errors='coerce')

plt.figure(figsize=(25, 15))
plt.bar(
    forest_fire_per_month['month'],
    forest_fire_per_month['number'],
    color=(0.5, 0.1, 0.5, 0.6)
)
plt.suptitle('Amazon Forest Fire over Months\n', fontsize=24)
plt.title('Using Data from Years 1998 to 2017\n', fontsize=20)
plt.xlabel('Month\n', fontsize=20)
plt.ylabel('Number of Forest Fires\n', fontsize=20)

for i, num in enumerate(forest_fire_per_month['number']):
    plt.text(
        i,
        num + 1000,
        int(num),
        ha='center',
        fontsize=15
    )

plt.setp(plt.gca().get_xticklabels(),
         rotation=45,
         horizontalalignment='right',
         fontsize=20)
plt.setp(plt.gca().get_yticklabels(), fontsize=20)

plt.tight_layout()
plt.show()


