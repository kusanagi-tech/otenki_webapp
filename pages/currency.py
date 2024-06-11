import streamlit as st
import requests as req
import pandas as pd

def currency():
  URL = """https://forex-api.coin.z.com/public/v1/ticker"""
  res = req.get(URL)
  ticker = res.json()['data']
  return ticker

df = pd.DataFrame(currency()).drop('status',axis=1)

st.header("💰外為相場📈",anchor='section1',divider='rainbow')

st.table(df)

st.divider()
st.markdown("[go to Top](#section1)")
