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
st.write("結局,GMOのコインのAPIを使いました。為替以上に相場が強烈に乱高下するので、レバレッジ取引はやめたほうがいいです。二番手はイーサリアム（ETH）です。暗号資産の投資信託が”海外で”承認されたので、去年よりイーサリアムは値上がりしています。")
st.write('https://diamond.jp/crypto/market/bitcoin-etf/')
st.markdown("[go to Top](#section1)")
