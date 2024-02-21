import yfinance as yf
import streamlit as st

st.write("""
# Простое приложение для отображения котировок акций

Отображаются цены закрытия и объем акций компании Apple!

""")

# Определение тикера
tickerSymbol = 'AAPL'
# Получение данных о котировках
tickerData = yf.Ticker(tickerSymbol)
# Получение исторических данных о ценах закрытия и объеме
tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-12-31')

# Отображение графика цен закрытия
st.write("## Цены закрытия")
st.line_chart(tickerDf.Close)

# Отображение графика объема торгов
st.write("## Объем торгов")
st.line_chart(tickerDf.Volume)