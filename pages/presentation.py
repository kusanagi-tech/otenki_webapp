import streamlit as st

st.header("✏️グラフ作成📈",anchor='section1',divider='rainbow')
st.image('images/zscore.png', caption='zscore')
st.code("""
Zスコアは、以下の式で計算できます。

Z = (X - μ) / σ
ここで、

Z は Zスコア
X は対象となるデータ値
μ はデータ全体の平均
σ はデータ全体の標準偏差
となります。

✨Google　スプレッドシートで使用した関数✨
=GOOGLEFINANCE("TRYJPY", "price", DATE(2024,1,1), DATE(2024,6,23), "daily")
=GOOGLEFINANCE("USDJPY", "price", DATE(2024,1,1), DATE(2024,6,23), "daily")
=STDEV.P(B4:B177)
=AVERAGE(B4:B177)
以上は絶対的な表記なので、相対的な表記にすると、  
=GOOGLEFINANCE("ETHJPY","price",TODAY()-30,TODAY())
こうすると日数が経過すると常に30日前から自動で再計算します。""")
st.divider()
st.markdown("[go to Top](#section1)")

st.image('images/btceth.png', caption='zscore2')
st.write("ビットコインとイーサリアムを、Zスコアで値下がり比率を比べるとほぼ同じ割合で下がっています。")
st.divider()
st.markdown("[go to Top](#section1)")
