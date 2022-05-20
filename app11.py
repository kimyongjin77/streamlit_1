from tkinter.font import names
from turtle import color
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

def main():
    #pass
    #스트림릿에서 재공하는 차트
    #line_chart, area_chart

    df1=pd.read_csv('data2/lang_data.csv')
    st.dataframe(df1)

    lang_list=df1.columns[1:]
    choice=st.multiselect('언어선택', lang_list)

    if len(choice) > 0:
        df_choice=df1[choice]
        st.dataframe(df_choice)

        #스트림릿이 제공하는 line_chart
        st.line_chart(df_choice)

        #스트림릿이 제공하는 area_chart
        st.area_chart(df_choice)

    df2=pd.read_csv('data2/iris.csv')
    st.dataframe(df2)
    #스트림릿이 제공하는 bar_chart
    st.bar_chart(df2.iloc[:,:4])

    #웹에서 사용할 수 있는 차트 라이브러리 중 
    # altair 챠트 : 스크림릿 설치시 자동으로 같이 설치된다.
    alt_chart=alt.Chart(df2).mark_circle().encode(
        x='petal_length', y='petal_width',
        color='species'
    )

    st.altair_chart(alt_chart)  #altair챠트를 사용하는 전용 함수

    #스트림릿이 map차트
    df3=pd.read_csv('data2/location.csv',index_col=0)   #위도,경도
    st.dataframe(df3)
    st.map(df3)

    # plotly 라이브러리를 이용한 차트 그리기.
    # plotly 챠트 , 많이 사용한다.
    # 설치 방법 : 새로은 터미널(커맨드프롬프트) 에서 또는 아마콘다 프롬프트 에서
    # pip install plotly==5.8.0
    # conda install -c plotly plotly=5.8.0

    df4=pd.read_csv('data2/prog_languages_data.csv', index_col=0)
    st.dataframe(df4)

    # plotly의 pie차트
    fig1=px.pie(df4, names='lang', values='Sum', title='각 언어별 파이차트')
    st.plotly_chart(fig1)

    # plotlt의 bar차트
    df4_sorted=df4.sort_values('Sum',ascending=False)
    fig2=px.bar(df4_sorted, x='lang', y='Sum')
    st.plotly_chart(fig2)


if __name__=='__main__':
    main()