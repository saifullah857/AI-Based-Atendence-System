import streamlit as st

from database.db import create_teacher
from src.components.header import header_dashboard, header_home
from src.components.footer import footer_dashboard, footer_home
from src.components.base_layout import style_background_dashboard, style_background_home,style_base_layout


def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    # ✅ Initialize session state
    if 'teacher_login_type' not in st.session_state:
        st.session_state['teacher_login_type'] = 'login'
    
    # ✅ Correct logic (removed duplicate call + fixed condition)
    if st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'registor':
        teacher_screen_registor()   

# Teacher Login Screen Section

def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("Go back to Home",type="secondary",icon=":material/arrow_back:",icon_position="left",shortcut="control+enter"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login using password",text_alignment="center")
    st.write("")   # ✅ replaced st.space()
    
    teacher_username = st.text_input("Username",placeholder="Saif Ullah")
    teacher_password = st.text_input("Password",type="password")
    
    st.divider()
    
    btn1,btn2=st.columns(2,gap="large")
    
    with btn1:
        st.button("Login",icon=":material/passkey:",icon_position="left",width="stretch",shortcut="control+enter")
        
    with btn2:      
        if st.button(" Register Instead ",icon=":material/passkey:",icon_position="left",type="primary",width="stretch",shortcut="control+enter"):
            st.session_state['teacher_login_type'] = 'registor'
            st.rerun()
            
    footer_dashboard()

# Teacher Register Screen Section

    def register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm):
    # ✅ Basic validation
        if not teacher_username or not teacher_name or not teacher_password or not teacher_password_confirm:
            return False, "All fields are required."
    
        if teacher_password != teacher_password_confirm:
            return False, "Passwords do not match."
        
        try:
            create_teacher(teacher_username, teacher_password, teacher_name)
            return True, "Registration successful!"
        except Exception as e:
            return False, f"Error creating teacher: {str(e)}"


def teacher_screen_registor():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("Go back to Home",type="secondary",icon=":material/arrow_back:",icon_position="left",shortcut="control+enter"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Registor your Teacher profile",text_alignment="left")
    
    st.write("")   # ✅ replaced st.space()
    
    teacher_username = st.text_input("Username",placeholder="saifi")
    teacher_name = st.text_input("Full Name",placeholder="Saif Ullah")
    teacher_password = st.text_input("Password",type="password")
    teacher_password_confirm = st.text_input("Confirm Password",type="password")
    
    st.divider()
    
    btn1,btn2=st.columns(2,gap="large")
    
    with btn1:
        if st.button("Registor Now",icon=":material/passkey:",icon_position="left",width="stretch",shortcut="control+enter"):
            success,message = register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm)
        
    with btn2:      
        if st.button(" Login Instead ",icon=":material/passkey:",icon_position="left",type="primary",width="stretch",shortcut="control+enter"):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()