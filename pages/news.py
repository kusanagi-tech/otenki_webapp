import streamlit as st
import requests as req
import pandas as pd

st.header("🎌 Japan NewsAPI",anchor='section1',divider='rainbow')

headers = {'X-Api-Key': st.secrets["NEWSAPI"]}
NEWSAPI = st.secrets["NEWSAPI"]
BASEURL = """https://newsapi.org/v2/top-headlines"""

category = { 
   "Headline": None,
   "Business": "business",
   "Sports": "sports",
   "Entertainments": "entertainment",
   "Science": "science",
   "Technology":"technology",

}

selection = st.selectbox("**ニュースを選択**", category , index = 0 )

if selection == "Headline":
  params = {'country':'jp'}
else:
  params = {'country':'jp', "category" : category[selection]}

res = req.get(BASEURL,headers=headers ,params=params)
news = res.json()

#見出しだけにしたい場合
#import pandas as pd
#df = pd.DataFrame(news["articles"])
#st.table(df['title'])

#URLを表示したい場合
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