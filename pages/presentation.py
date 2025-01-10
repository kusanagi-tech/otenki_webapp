import streamlit as st

st.header("✏️グラフ作成📈",anchor='section1',divider='rainbow')
st.image('images/nikkei0110.png', caption='一ヶ月の日経平均株価の動き、やや頭打ちの相場')
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
st.image('images/coin16.png', caption='zscore2')
st.write("""米司法省が69,370 BTC（約1兆円相当）のビットコインを売却する許可を裁判所から得たとの報道で下落  
         https://coinpost.jp/?p=586225""")

st.divider()
st.markdown("[go to Top](#section1)")

st.image('images/gaitame250110.png', caption='zscore3')
st.write("""
         円安傾向だが、ポンドがやや下がり気味
""")

st.divider()
st.markdown("[go to Top](#section1)")
