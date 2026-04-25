import streamlit as st

from src.components.header import header_dashboard, header_home
from src.components.footer import footer_home
from src.components.base_layout import style_background_dashboard, style_background_home,style_base_layout

def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    teacher_screen_registor()
    
    
    
def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home",type="secondary",icon=":material/arrow_back:",icon_position="left",on_click=lambda: st.session_state.update({'login_type':None}),shortcut="backspace")
    st.header("Registor your Teacher profile")
    
def teacher_screen_registor():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home",type="secondary",icon=":material/arrow_back:",icon_position="left",on_click=lambda: st.session_state.update({'login_type':None}),shortcut="backspace")
    st.header("Registor your Teacher profile")
