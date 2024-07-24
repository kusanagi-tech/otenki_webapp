import streamlit as st

st.header("✏️グラフ作成📈",anchor='section1',divider='rainbow')
st.image('images/tyo.png', caption='zscore')
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
たとえばJT（日本たばこ産業）"2914.T"と東京エレクトロン"8035.T"の株を同じ金額で買ったら、どちらが得だったのか？というのがわかります。  

見当がつくと思いますが、2024年3-4月の時点では東京エレクトロンの方が得、2024年7月の時点ではJTの方が得だったということがわかります。
""")
st.divider()
st.markdown("[go to Top](#section1)")
st.image('images/coin3.png', caption='zscore2')
st.write("暗号資産相場はトランプ相場で返り咲き")

st.divider()
st.markdown("[go to Top](#section1)")

st.image('images/gaitame240725.png', caption='zscore3')
st.write("""
         2024年７月22〜25日の為替のZスコア（時系列はUTC）  
         円高進行　一時1ドル＝153円台前半に　日銀の利上げ観測が影響か  
         https://youtu.be/zJQu9F0EfOs?si=1e1aa8_tJcPzPztO""")

st.divider()
st.markdown("[go to Top](#section1)")

