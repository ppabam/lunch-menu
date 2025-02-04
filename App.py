import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("순신점심기록장")
st.subheader("입력")
menu_name = st.text_input("메뉴 이름", placeholder="예: 김치찌게")
member_name = st.text_input("먹은 사람", value="TOM")
dt = st.date_input("얌얌 날짜")












st.subheader("통계")
df = pd.read_csv('note/menu.csv')

start_idx = df.columns.get_loc('2025-01-07')
melted_df = df.melt(id_vars=['ename'], value_vars=df.columns[start_idx:-2], 
                     var_name='dt', value_name='menu')

not_na_df = melted_df[~melted_df['menu'].isin(['-','x','<결석>'])]
gdf = not_na_df.groupby('ename')['menu'].count().reset_index()
#gdf.plot(x="ename", y="menu", kind="bar")

gdf

# 📊 Matplotlib로 바 차트 그리기
# https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
fig, ax = plt.subplots()
gdf.plot(x="ename", y="menu", kind="bar", ax=ax)
st.pyplot(fig)
