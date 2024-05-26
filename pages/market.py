import streamlit as st
import pandas as pd
import numpy as np

st.header("🇹🇷 トルコリラスワップ試算",anchor='section1',divider='rainbow')

#プルダウンセレクターで計算する。
# leverage = st.selectbox(
#     "レバレッジは何倍にする？",
#     (2, 3, 4, 5, 10, 25))

#スライダーで計算する
leverage = st.select_slider(
    "**レバレッジは何倍にする？**(1〜25倍:0.5単位)",options=np.arange(1,25.5,0.5),value = 3.0)

swap = 35 
souba = 4.85
yosan = int(souba*10000/leverage)

nakami = np.array([swap,swap*30,swap*365,yosan] )
tuuka = [1,3,5,10,20,30,40,50,60,70,80,90,100]
kanji = "万通貨"

mydata=[]
for i in tuuka:
    mydata.append(nakami*i) 

index  = [ str(i) + kanji for i in tuuka ]
colmns = ["日額","月額","年額",f"予算（レバ{leverage}倍）"]
yukou =  mydata[0][3]/2000*100

df = pd.DataFrame(data=mydata, index = index, columns = colmns)

st.write(f":red[**レバレッジ{leverage}倍**], **単価 {souba}円 、スワップ{swap}円:green[ 有効比率 {yukou:.2f}%]**  (100%を切るとロスカット)")
st.table(df.style.format('{:,d}'))
st.write("大体の目安です。numpyを使うと、配列全体の乗算ができます。小数点でstepの指定ができます。")
st.markdown("[go to Top](#section1)")


