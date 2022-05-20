##파일을 분리해서 만드는 앱
##복잡도가 있는 소스코드를 효율적으로 개발 및 관리
import streamlit as st
from app9_about import run_about
from app9_eda import run_eda
from app9_home import run_home
from app9_ml import run_ml

def main():
    #pass
    st.title('파일 분리 앱')

    menu=['Home','EDA','ML','About']
    choice=st.sidebar.selectbox('메뉴',menu)

    if choice==menu[0]:
        #pass
        #from app9_home import run_home 하여 함수 사용 가능하다.
        run_home()
    elif choice==menu[1]:
        #pass
        run_eda()
    elif choice==menu[2]:
        #pass
        run_ml()
    elif choice==menu[3]:
        #pass
        run_about()


if __name__=='__main__':
    main()