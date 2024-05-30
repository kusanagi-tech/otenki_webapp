import streamlit as st
import feedparser
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.data.jma.go.jp/developer/xml/feed/eqvol_l.xml'
d_atom = feedparser.parse(URL)
count = len(d_atom['entries'])

mydata = []
myurl = []

for i in range(count):
  base = d_atom['entries'][i]
  mydata.append(base['summary']+base['updated'])
  myurl.append(base['links'][0]['href'])

data = zip(mydata,myurl)

kazan = {
  "最新10件": '',
  "桜島":"さくらじま",
  "薩摩硫黄島":"さつまいおうじま",
  "口永良部島":"くちのえらぶじま",
  "諏訪之瀬島":"すわのせじま",
  "浅間山":"あさまやま",
  "阿蘇山":"あそさん",
  "震源・震度情報": ""
}

st.header("🌋地震火山情報XML",anchor='section1',divider='rainbow')
mountain = st.selectbox("**火山を選択**",kazan,index = 0 )

def linkurl(x):
   r = requests.get(x)
   soup = BeautifulSoup(r.text.encode(r.encoding),'lxml-xml')
   koumoku = []

   tags = ["Title","ReportDateTime","Headline","""jmx_eb:Coordinate""","Name","""jmx_eb:Magnitude""",'ForecastComment']

   for a in tags :
      if a == "Headline":
        koumoku.append(soup.find(a).find("Text").get_text()) 
      elif a == """jmx_eb:Coordinate""":
        koumoku.append(soup.find(a).get("description") )
        koumoku.append(soup.find(a).get_text()) 
      elif a == """jmx_eb:Magnitude""":
        koumoku.append("M "+soup.find(a).get_text())      
      else:
        koumoku.append(soup.find(a).get_text())
   return st.table(koumoku)

def button(keyword):
  keyword = keyword.reset_index(drop=True)
  if st.button(":blue[**詳細情報**]",key=1):
    for i in range(0,10) :
      linkurl(keyword.loc[i,'URL'])
      st.write(keyword.loc[i,'URL'])
    st.markdown("[go to Top](#section1)")

meisyou = f'{mountain} : {kazan[mountain]}'
df = pd.DataFrame(data = data,columns=[meisyou,"URL"])
keyword = df[df[meisyou].str.contains(mountain)]

if mountain == "最新10件" :
  st.table(df[meisyou].head(10))
elif mountain == "震源・震度情報" : 
  button(keyword)
  st.table(keyword[meisyou].head(10)) 
else :
  st.table(keyword[meisyou].head(10))

st.write("""出典：気象庁 https://xml.kishou.go.jp/xmlpull.html""")
st.write("""最新の情報は上から追加され下に押し出されます。（時系列なので同じ場所が違う時間で何度も掲載されています。）parser はXMLではなくAtom 向けの feedparser を使わないとデーターが取れません。""")
st.divider()
st.markdown("[go to Top](#section1)")

