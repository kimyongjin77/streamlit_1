import matplotlib.pyplot as plt
from numpy import var
import seaborn as sb
import streamlit as st
import pandas as pd

def main():
    #pass
    st.title('차트그리기1')

    df=pd.read_csv('data2/iris.csv')
    st.dataframe(df)

    #차트그리기
    #sepal_length 와 sepal_width의 관계를
    #챠트로 나타내시오

    #plt.scatter
    #브라우져의 차트영역을 잡아준다.
    fig=plt.figure()
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('sepal_length VS sepal_width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    st.pyplot(fig)

    #sb.scatterplot
    fig2=plt.figure()
    sb.scatterplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig2)

    #sb.regplot
    fig3=plt.figure()
    sb.regplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig3)

    #sepal_length 로 히스토그램
    #bin 개수는 20
    fig4=plt.figure()
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.8)
    st.pyplot(fig4)

    #sepal_length 히스토그램을 그리되,
    #bin의 개수를 10개와 20개로
    #두개의 차트를 수평으로 보여주기
    fig5=plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.hist(data=df, x='sepal_length', bins=10, rwidth=0.8)
    plt.subplot(1,2,2)
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.8)
    st.pyplot(fig5)

    #species 컬럼의 데이터를 각각 몇개씩 있는지
    #차트를 나타내시오
    fig6=plt.figure()
    sb.countplot(data=df, x='species')
    st.pyplot(fig6)

    #지금까지 한건, plt와 seaborn차트를
    #streamlit에 그리는 방법을 했다..

    #데이터프레임이 제공하는 차트함수도
    #streamlit에 그릴 수 있다.

    #species는 각각 몇개인지, 데이터프레임의 차트로 그리는 방법
    fig7=plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig7)

    #sepal_length컬럼을 데이터프레임 히스토그램 차트로 그리는 방법
    fig8=plt.figure()
    df['sepal_length'].hist(bins=40)
    st.pyplot(fig8)





if __name__=='__main__':
    main()