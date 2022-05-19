import streamlit as st
import pandas as pd

def main():
    #pass   #코딩이 없으면
    df=pd.read_csv('data2/iris.csv')
    #print(df)

    #버튼만들기
    if st.button('데이터보기') :    #클릭하면 True를 리턴.
        st.dataframe(df)

    #'대문자' 버튼을 만들고 버튼을 누르면, speices 컬럼의 값들을 대문자로
    #변경한 데이터 프레임을 보여주세요.
    if st.button('대문자'):
        #st.dataframe(df['species'].str.upper())
        df['species']=df['species'].str.upper()
        st.dataframe(df)

    #라디오버튼 : 여러개중에 한개 선택할때
    my_order=['오름차순 정렬','내림차순 정렬']
    status=st.radio('정렬방법 선택', my_order)  #클릭하면 텍스트를 리턴.
    #print(status)
    if status==my_order[0]:
        # petal_length 컬럼을 오름차순 정렬
        st.dataframe(df.sort_values('petal_length'))
    elif status==my_order[1]:
        # petal_length 컬럼을 내림차순 정렬
        st.dataframe(df.sort_values('petal_length', ascending=False))

    status2=st.radio('정렬방법 선택2', my_order)  #클릭하면 텍스트를 리턴.

    #체크박스 체크/해제
    if st.checkbox('헤드 5개만 보기'):  #체크하면 True 해제하면 False 리턴.
        st.dataframe(df.head())
    else:
        st.text('헤드 숨기기')

    #셀렉트박스 : 여러개에서 한개만 고르는 UI
    language=['python','C','java','Go','php']
    my_choice=st.selectbox('좋아하는 언어 선택', language)   #선택하면 텍스트를 리턴.
    if my_choice==language[0]:
        st.write(language[0] + '을 선택했어요')
    elif my_choice==language[1]:
        st.write(language[1] + '을 선택했어요')

    #멀티셀렉트박스 : 여러개에서 여러개 선택하는 UI
    st.multiselect('여러개 선택가능',language)

    #멀티셀렉트를 이용해서, 특정 컬럼들만 가져오기
    #유저에게, iris df의 컬럼들을 다 보여주고,
    #유저가 선택한 컬럼들만, 데이터프레임을 화면에 보여줄것..
    column_list=df.columns
    choice_list=st.multiselect('컬럼을 선택하세요', column_list)    #선택할때마다 선택한것을 리스트로 리턴
    #print(choice_list)
    st.dataframe(df[choice_list])
    
    #슬라이더 : 숫자 조정하는데 주로 사용
    #st.slider('나이',1.0,120.0,30,0.1)
    age=st.slider('나이',1,120,30)      #클릭한 숫자 리턴
    st.text('선택한 나이는 {}입니다.'.format(age))

    #익스펜더
    with st.expander('익스펜더'):
        st.text('안녕하세요.')
        st.dataframe(df)
        


if __name__=='__main__':
    main()