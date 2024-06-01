import streamlit as st
import requests as req

st.header("🎌 Japan NewsAPI",anchor='section1',divider='rainbow')


NEWSAPI = st.secrets["NEWSAPI"]
BASEURL = """https://newsapi.org/v2/top-headlines?country=jp&"""
BASEURL2 = """https://newsapi.org/v2/top-headlines?country=jp&category="""

category = { 
   "Headline": BASEURL+"""apiKey="""+NEWSAPI,
   "Business": BASEURL2+"""business&apiKey="""+NEWSAPI,
   "Sports": BASEURL2+"""sports&apiKey="""+NEWSAPI,
   "Entertainments": BASEURL2+"""entertainment&apiKey="""+NEWSAPI,
   "Science": BASEURL2+"""science&apiKey="""+NEWSAPI,
   "technology": BASEURL2+"""technology&apiKey="""+NEWSAPI,

}

params = st.selectbox("**ニュースを選択**", category,index = 0 )
res = req.get(category[params])
news = res.json()

#st.write(news)

keys = ['title','url' ]
count = len(news['articles'])
for n in range(count):
  for i in keys:
    base = news['articles'][n]
    if i == 'title':
        st.write(f"**🟩 { base[i]}**  {base['publishedAt']}")
    else:
        st.write(f"{base[i]}   ")
st.divider()
st.markdown("[go to Top](#section1)")