import streamlit as st
import feedparser
import pandas as pd

d_atom = feedparser.parse('https://www.data.jma.go.jp/developer/xml/feed/eqvol_l.xml')
count = len(d_atom['entries'])
mydata = []

for i in range(count):
  base = d_atom['entries'][i]
  mydata.append(base['summary']+base['updated'])

st.header("🌋地震火山情報XML",anchor='section1',divider='rainbow')

mountain = st.radio("**火山を選択**",
    ["最新10件", "桜島", "薩摩硫黄島","口永良部島","諏訪之瀬島","浅間山","阿蘇山"],index = 0 )

df = pd.DataFrame(data = mydata,columns=[mountain])
keyword = df[df[mountain].str.contains(mountain)]

if mountain == "最新10件" :
  st.table(df.head(10))
else :
  st.table(keyword.head(10))

st.write("""出典：気象庁 https://xml.kishou.go.jp/xmlpull.html""")
st.write("""最新の情報は上から追加され下に押し出されます。（時系列なので同じ場所が違う時間で何度も掲載されています。）parser はXMLではなくAtom 向けの feedparser を使わないとデーターが取れません。""")
st.divider()
st.markdown("[go to Top](#section1)")
