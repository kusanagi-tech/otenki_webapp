import streamlit as st
import requests as req
import pandas as pd
import datetime

url = """https://api.coin.z.com/public/"""
ticker = "v1/ticker"

symbols = [
'BTC',
'ETH',
'BCH',
'LTC',
'XRP',
'XEM',
'ASTR',
'XLM',
'BAT',
'XTZ',
'QTUM',
'ENJ',
'DOT',
'ATOM',
'MKR',
'DAI',
'XYM',
'MONA',
'FCR',
'ADA',
'LINK',
'DOGE',
'SOL',
]

st.header("🪙暗号資産相場📈",anchor='section1',divider='rainbow')

#セッションの高速化
s = req.Session()

price =[]
for i in range(len(symbols)):
  param ={"symbol":symbols[i]}
  coin = s.get(url+ticker,params=param)
  format = float(coin.json()['data'][0]['last'])
#  price.append(f"{format:,}")
  price.append(format)

pd.options.display.float_format = '{:,}'.format
df = pd.DataFrame(price,index=symbols,columns=['LastPrice'])

now = datetime.date.today()

st.text(now)
st.text(df.sort_values('LastPrice',ascending=False))

st.divider()
st.write('暗号資産は税金の計算に要注意です。')
st.write("https://youtu.be/lq1z_6DeWDM?si=roswKKHCEk66e9iP")

st.markdown("[go to Top](#section1)")
