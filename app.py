import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of APPLE!

""")


tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2050-5-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
