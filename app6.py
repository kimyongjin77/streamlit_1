from numpy import empty, mask_indices
import streamlit as st

def main():
    #pass
    #유저한테 입력 받는 방법
    #1.이름(텍스트)을 입력 받기
    name=st.text_input('이름을 입력하세요') #입력한 텍스트 리턴
    if name != '':
        st.subheader(name + '님 안녕하세요?')
    
    #2.입력글자갯수제한
    name=st.text_input('주소을 입력하세요',max_chars=10)

    #3.여러 행을 입력
    message=st.text_area('메세지를 입력하세요', height=3)
    st.subheader(message)

    #4.숫자입력, 정수
    st.number_input('숫자입력', 1, 100)

    #5.숫자입력, 실수
    st.number_input('숫자입력',1.0, 100.0, step=0.1)

    #6.날짜입력
    my_date=st.date_input('날짜입력')
    st.write(my_date)
    #요일출력
    st.write(my_date.weekday())
    st.write(my_date.strftime('%A'))
    
    #7.시간입력
    my_time=st.time_input('시간입력')
    st.write(my_time)

    #8.색깔입력
    color=st.color_picker('색을 입력')
    st.write(color)

    #9.비밀번호입력
    pwd=st.text_input('암호입력',type='password')
    st.write(pwd)

if __name__=='__main__':
    main()