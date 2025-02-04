import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello **world!**

![img](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMDmITYUL3-dQiE99pPRG-f1gLO76Wh_UjEXTSvx0RiNdbvu_d4-L5OR43qlce8eNfeHld83WgawlwjNkQvWM7cA)
""")

df = pd.read_csv('note/menu.csv')
df

