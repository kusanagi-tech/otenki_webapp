import streamlit as st

st.header("✏️グラフ作成📈",anchor='section1',divider='rainbow')
st.image('images/nikkei1005.png', caption='乱高下している日経平均株価の動き')
st.code("""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#銘柄を代入
ticker = ["2914.T","8035.T"]
#ticker = ["AAPL","MSFT","GOOG","AMZN","META","NVDA","TSLA"]
#ticker =["USDJPY=X","NZDJPY=X"]

count = len(ticker)
data ={}

for i in range(count):
  data[ticker[i]]=yf.download(ticker[i],period="6mo",interval="1d").Close

def zscore(x):
  stdev = np.std(x)
  zdata = (x-np.mean(x))/stdev
  return zdata

#scipyモジュールを使用する方法
# import scipy.stats as stats 
# def zscore(x):
#   zdata = stats.zscore(x)
#   return zdata

#相場(終値）をそのまま出力する場合
# def zscore(x):
#   zdata = x
#   return zdata

plt.figure(figsize=(10,5))
plt.title(f"Zscore {ticker}")
plt.ylabel("Price")
plt.xlabel("Date")

#Xラベルを回転させたい場合
#plt.xticks(rotation=45)

for i in data.keys():
  plt.plot(zscore(data[i]),label=i)
plt.legend()
plt.show()
""")
st.write("""
Zスコアは、以下の式で計算できます。  

Z = (X - μ) / σ  
ここで、  

Z は Zスコア  
X は対象となるデータ値  
μ はデータ全体の平均  
σ はデータ全体の標準偏差  
となります。  

Zスコアは単位が違うものを比較評価するために使います。  
""")
st.divider()
st.markdown("[go to Top](#section1)")
st.image('images/coin8.png', caption='zscore2')
st.write("暗号資産の動き")

st.divider()
st.markdown("[go to Top](#section1)")

st.image('images/gaitame241005.png', caption='zscore3')
st.write("""
         2024年9月30日〜の為替のZスコア（時系列はUTC）  

        ◆10月4日の米雇用統計の発表で、円安ドル高が進行。  
        https://youtu.be/Kv7Qfhr5X80?si=vm5Lsa7utw0nFQ0y  
        ◆米雇用統計カウントダウン（21：30分）  
        https://www.youtube.com/live/FEKU0lX7JeI?si=_AqLxmvUafqKFjCl&t=1740          
        ◆石破ショック回避策「利上げする環境にない」  
         https://youtu.be/eSTDB0S-AFo?si=iHQI5WiKZYFF7-2c  
         円高になると日本の株価がさがるという状況を回避しないといけないのです。
""")

st.divider()
st.markdown("[go to Top](#section1)")

