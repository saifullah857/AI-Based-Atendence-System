import streamlit as st

from src.components.base_layout import style_background_dashboard, style_background_home,style_base_layout

def home_screen():
    st.header("Snap Class")
    
    style_background_home()
    
    style_base_layout()
    col1,col2 = st.columns(2,gap='small')
    with col1:
        if st.button("Login as Teacher",type="secondary"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    with col2:
        if st.button("Login as Student"):
            st.session_state['login_type'] = 'student'
            st.rerun()                        