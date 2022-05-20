import streamlit as st
import pandas as pd

def run_eda():
    #pass
    st.subheader('EDA 화면입니다.')

    df=pd.read_csv('data2/iris.csv')
    #컬럼이름을 보여주시고,
    #여러 컬럼들 선택 가능토록 하여 선택한 컬럼들만 화면에 보여줍니다.
    #상관계수를 구하여 화면에 보여줍니다.
    
    st.subheader('iris 데이터')
    menu=df.columns
    choice=st.multiselect('컬럼 선택', menu)
    if len(choice) > 0:
        st.dataframe(df[choice])

    st.text('상관계수')
    if len(choice) > 0:
        st.dataframe(df[choice].corr())