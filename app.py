import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.write("""# Секретные данные о чаевых в ресторанах """)

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
#path = '../learning/datasets/tips.csv'
tips = pd.read_csv(path)

st.write("""## Загрузка данных""")
st.write(tips)

st.write("""## График чаевых по времени""")
tip_time = tips.groupby('time')['tip'].sum()
st.bar_chart(tip_time)

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(tips['total_bill'], bins=20, color='orange', edgecolor='black')
ax.set_title('Гистограмма общей суммы счета')
ax.set_xlabel('Сумма счета')
ax.set_ylabel('Частота')
st.pyplot(fig)

st.write("""## Диаграмма рассеяния общей суммы счета и размера чаевых""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', palette='pastel', s=50, ax=ax)
st.pyplot(fig)

st.write("""## Диаграмма рассеяния общей суммы счета и размера чаевых с разделением по полу""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', palette='Set2', s=50, ax=ax)
st.pyplot(fig)

st.write("""## Сумма счетов по дням""")
day_total_bill = tips.groupby('day')['total_bill'].sum()
st.bar_chart(day_total_bill)

st.write("""## Чаевые в зависимости от дня и пола""")
fig, ax = plt.subplots()
sns.boxplot(data=tips, x='day', y='tip', hue='sex', palette='husl', ax=ax)
st.pyplot(fig)

st.write("""## Чаевые за обед и ужин""")
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
sns.histplot(data=tips[tips['time'] == 'Lunch'], x='tip', bins=10, color='pink', ax=axes[0])
axes[0].set_title('Чаевые за обед')
axes[0].set_xlabel('Размер чаевых')
axes[0].set_ylabel('Частота')

sns.histplot(data=tips[tips['time'] == 'Dinner'], x='tip', bins=10, color='green', ax=axes[1])
axes[1].set_title('Чаевые за ужин')
axes[1].set_xlabel('Размер чаевых')
axes[1].set_ylabel('Частота')

st.pyplot(fig)
st.write("Анализ завершен!", text_color="green")



