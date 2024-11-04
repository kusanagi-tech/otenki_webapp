import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re

st.header("🇺🇸ドル増減率計算",anchor='section1',divider='rainbow')

title = st.text_input("**シンボルを入力してリターンキーを押す**", "USDJPY=X")
findn = re.match('[0-9]{4}', title, flags=0)

#銘柄を代入
ticker = []
if findn:
  ticker = [title +'.T']
else:
  ticker = [title.upper()]

count = len(ticker)
data ={}

days = st.number_input( "**日数を入力**",value=14,step=1)

st.info("""入力例 ) 日本株式：四桁の数字　暗号資産：BTC-JPY　為替：USDJPY=X  
        日経平均： ^N225　米国株式のシンボル：AAPL ^GSPC　使用モジュールyfinance
        """)

#期間の計算
start = datetime.date.today() - datetime.timedelta(days=days)
end = datetime.date.today() 

for i in range(count):
  data[ticker[i]]=yf.download(ticker[i],start = start,end = end,interval="1d").Close

#相場(終値）をそのまま出力する場合
def zscore(x):
  zdata = x
  return zdata

plt.figure(figsize=(10,5))
plt.title(f"{ticker}")
plt.ylabel("Price")
plt.xlabel("Date")

#Xラベルを回転させたい場合
plt.xticks(rotation=45)

for i in data.keys():
  plt.plot(zscore(data[i]),label=i)
plt.legend()
plt.grid()
st.pyplot(plt)

pd.options.display.float_format = '{:.3f}'.format
a = data[i]
average = a.sum()/len(a)
stdev = np.std(a)
per = 100-(a[0]/a[-1]*100)

st.write(F"**📝{ticker} 相場：{days}日前からの終値（自動更新）**")

if per > 0:
  st.write(f"**平均{average:.2f}　標準偏差{stdev:.4}　増減率 :blue[{per:.4}％]**")
else:
  st.write(f"**平均{average:.2f}　標準偏差{stdev:.4}　増減率 :red[{per:.4}％]**")

#st.write("average:",round(average,3),"stdev:",round(stdev,4))
st.text(a)

st.divider()
st.markdown("[go to Top](#section1)")

