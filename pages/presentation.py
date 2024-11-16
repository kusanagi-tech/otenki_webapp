import streamlit as st

st.header("✏️グラフ作成📈",anchor='section1',divider='rainbow')
st.image('images/nikkei1117.png', caption='一ヶ月の日経平均株価の動き 温泉株が躍進')
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
st.image('images/coin12.png', caption='zscore2')
st.write("リップルの上昇が顕著")

st.divider()
st.markdown("[go to Top](#section1)")

st.image('images/gaitame241117.png', caption='zscore3')
st.write("""
         ドル優勢、ユーロ劣勢、トルコリラはドルと連動しているので上昇  
         ◆暗号資産相場は、全体的に上昇していますが、首位のビットコインの単価が高いので、３番手４番手のライトコインやリップルが買い貯めされています。ライトコインやビットコインキャッシュはビットコインと構造が似ています。リップルは独自構造で、送金の速さが売りです。これは上位にランクインしています。
""")

st.divider()
st.markdown("[go to Top](#section1)")

