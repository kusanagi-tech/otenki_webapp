import streamlit as st

st.header("✏️グラフ作成📈",anchor='section1',divider='rainbow')
st.image('images/tyo.png', caption='zscore')
st.code("""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = ["2914.T","8035.T"] #比較銘柄を代入
data0 = yf.download(ticker[0],period="6mo",interval="1d")
data1 = yf.download(ticker[1],period="6mo",interval="1d")

def zscore(x):
  stdev = np.std(x)
  data = (x-np.mean(x))/stdev
  return data

plt.figure(figsize=(10,5))
plt.title(f" {ticker[0]} and {ticker[1]} Zscore")
plt.ylabel("Price")
plt.xlabel("Date")
plt.plot(zscore(data0.Close),label=ticker[0])
plt.plot(zscore(data1.Close),label=ticker[1])
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

見当がつくと思いますが、2024年7月の時点ではJTの方が得だったということがわかります。
""")
st.divider()
st.markdown("[go to Top](#section1)")

st.image('images/btceth.png', caption='zscore2')
st.write("ビットコインとイーサリアムを、Zスコアで値下がり比率を比べるとほぼ同じ割合で下がっています。")
st.divider()
st.markdown("[go to Top](#section1)")
st.image('images/btcusd.png', caption='zscore3')
st.write("ビットコインと米ドルを、Zスコアで比べると騰落は、ほぼ同じ割合で反転しています。")
st.divider()
st.markdown("[go to Top](#section1)")
