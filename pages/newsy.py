import streamlit as st
import requests as req
from bs4 import BeautifulSoup

st.header("🌎 Yahoo news headline",anchor='section1',divider='rainbow')

# Yahoo!ニュースのトップページにアクセス
url = "https://news.yahoo.co.jp/"
res = req.get(url)

# HTMLを解析
soup = BeautifulSoup(res.content, "html.parser")

# ヘッドラインを取得
headlines = soup.find_all("a", class_="sc-1nhdoj2-1 hKGArG")

# ヘッドラインを表示
count = len(headlines)

for i in range(count):
    st.page_link(headlines[i].get('href'), label = headlines[i].text, icon="🍋")

st.write('\n 参照元: ',url)

st.divider()
st.markdown("[go to Top](#section1)")
