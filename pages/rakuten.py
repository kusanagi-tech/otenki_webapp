import streamlit as st
import requests as req

URL = "https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426"
APP_ID = st.secrets["rakutenAPI"]

st.header("🧳✈ 楽天トラベルAPI🏝️🍧",anchor='section1',divider='rainbow')

#場所を代入
place = st.text_input("**場所を入力してリターンキーを押す**", "新宿区")
if place == "":
    st.write("場所を入力して下さい。")
    exit()

params = {
    'applicationId':APP_ID,
    'keyword':place,
    'page':1,
    'sort':'+roomCharge'
}

res  = req.get(URL,params)
#デバッグ用
# res.status_code
#res.json()

#hotelsの変数に全データーが入る
hotels = res.json()['hotels']
count = len(hotels)

st.write(f"{place}エリア 総件数: {count}件"+"\n")
for i in range(count):
    basic = hotels[i]['hotel'][0]['hotelBasicInfo']
    st.write(f"""
    **◆ { basic['hotelName']}** 
    - { basic['hotelSpecial']}  
    Access: {basic['access']}  
    Address: { basic['address2']} tel: { basic['telephoneNo']}  
    URL: { basic['hotelInformationUrl']}  
    """)
    st.markdown("[go to Top](#section1)")

st.divider()