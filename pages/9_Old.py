import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from lunch_menu.db import get_connection, db_name, insert_menu, select_table

st.set_page_config(page_title="Old", page_icon="💀")
st.markdown("# 💀 Old Page")
st.sidebar.header("Old Page")

members = {"SEO": 5, "TOM": 1, "cho": 2, "hyun": 3, "nuni": 10, "JERRY": 4, "jacob": 7, "jiwon": 6, "lucas": 9, "heejin": 8}

st.subheader("입력")
menu_name = st.text_input("메뉴 이름", placeholder="예: 김치찌게")
member_name = st.selectbox(
    "먹은 사람",
    options=list(members.keys()),
    index=list(members.keys()).index('TOM')
)
member_id = members[member_name]

dt = st.date_input("얌얌 날짜")

isPress = st.button("메뉴 저장")

if isPress:
    # member_name 을 member_id 로 바꾸어서 DB 에 id 가 insert 되록 해주세요
    if menu_name and member_id and dt:
        if insert_menu(menu_name, member_id, dt):
            st.success(f"입력성공")
        else:
            st.error(f"입력실패")
    else:
        st.warning(f"모든 값을 입력해주세요!")


st.subheader("확인")
select_df = select_table()
select_df

st.subheader("통계")
gdf = select_df.groupby('ename')['menu'].count().reset_index()
gdf

st.subheader("차트")
# https://docs.streamlit.io/develop/api-reference/charts/st.pyplot
try:
    fig, ax = plt.subplots()
    gdf.plot(x="ename", y="menu", kind="bar", ax=ax)
    st.pyplot(fig)
except Exception as e:
    st.warning(f"차트를 그리기에 충분한 데이터가 없습니다")
    print(f"Exception:{e}")

st.subheader("벌크 인서트")
if st.button("한방에 인서트"):
    df = pd.read_csv('note/menu.csv')
    start_idx = df.columns.get_loc('2025-01-07')
    melted_df = df.melt(id_vars=['ename'], value_vars=df.columns[start_idx:-2], 
                     var_name='dt', value_name='menu')
    
    not_na_df = melted_df[~melted_df['menu'].isin(['-','x','<결석>'])]

    # TODO 아래 메시지를 성공/실패 구분
    # 모두 성공했으면 성공 / 모두 성공하지 않은 경우는
    for _, row in not_na_df.iterrows():
        m_id = members[row['ename']]
        insert_menu(row['menu'], m_id, row['dt'])
    # IF 총건수 == 성공건수가 같으면, 또는 실패가 없으면 st.success
        # st.success(f"벌크인서트 성공")
    # ELES
        # 에러메시지 출력 -> 총건 00 중 00 실패

