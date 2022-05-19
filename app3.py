import streamlit as st
import pandas as pd

def main():
    #pass   #코딩이 없으면
    df=pd.read_csv('data2\iris.csv')
    #print(df)
    st.dataframe(df)    #df데이터프레임을 브라우져에 출력

    species=df['species'].unique()
    st.text('아이리스 꽃은' + species + '으로 되어 있다.')

    st.dataframe(df.head())
    st.write(df.head())


if __name__=='__main__':
    main()