import streamlit as st

from src.database.db import create_teacher, teacher_login
from src.database.db import check_teacher_exist
from src.components.header import header_dashboard, header_home
from src.components.footer import footer_dashboard, footer_home
from src.components.base_layout import style_background_dashboard, style_background_home,style_base_layout


def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    
    if "teacher_data" in st.session_state:
        teacher_dashborad()
        return   # 🔥 FIX: stop further rendering
    
    elif 'teacher_login_type' not in st.session_state:
        st.session_state['teacher_login_type'] = 'login'
        
    
    if st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'registor':
        teacher_screen_registor()   


def teacher_dashborad():
    teacher_data = st.session_state.teacher_data
    
    st.header(f"Welcome back, {teacher_data['username']}!", text_alignment="center")
    st.success("You are now logged in!")   # optional message
    st.write("This is your teacher dashboard. You can manage your classes, view student progress, and more.")
    

def login_teacher(username,password):
    if not username or not password:
        return False
    
    teacher = teacher_login(username,password)
    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True


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
    st.write("")
    
    teacher_username = st.text_input("Username",placeholder="Saif Ullah")
    teacher_password = st.text_input("Password",type="password")
    
    st.divider()
    
    btn1,btn2=st.columns(2,gap="large")
    
    with btn1:
        if st.button("Login",icon=":material/passkey:",icon_position="left",width="stretch",shortcut="control+enter"):
            if login_teacher(teacher_username,teacher_password):
                st.toast("Login successful!",icon="👋")
                st.session_state['teacher_info'] = {
                    'username': teacher_username
                }
                st.rerun()  
            else:
                st.error("Invalid username or password.")
        
    with btn2:      
        if st.button(" Register Instead ",icon=":material/passkey:",icon_position="left",type="primary",width="stretch",shortcut="control+enter"):
            st.session_state['teacher_login_type'] = 'registor'
            st.rerun()
            
    footer_dashboard()


# Register logic
def register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm):
    if not teacher_username or not teacher_name or not teacher_password or not teacher_password_confirm:
        return False, "All fields are required."
        
    if check_teacher_exist(teacher_username):
        return False, "Username already exists. Please choose a different one."
    
    if teacher_password != teacher_password_confirm:
        return False, "Passwords do not match."
        
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Registration successful!"
    except Exception as e:
        return False, f"Error creating teacher: {str(e)}"


# Teacher Register Screen Section
def teacher_screen_registor():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("Go back to Home",type="secondary",icon=":material/arrow_back:",icon_position="left",shortcut="control+enter"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Registor your Teacher profile",text_alignment="left")
    
    st.write("")
    
    teacher_username = st.text_input("Username",placeholder="saifi")
    teacher_name = st.text_input("Full Name",placeholder="Saif Ullah")
    teacher_password = st.text_input("Password",type="password")
    teacher_password_confirm = st.text_input("Confirm Password",type="password")
    
    st.divider()
    
    btn1,btn2=st.columns(2,gap="large")
    
    with btn1:
        if st.button("Registor Now",icon=":material/passkey:",icon_position="left",width="stretch"):
            success,message = register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
        
    with btn2:      
        if st.button(" Login Instead ",icon=":material/passkey:",icon_position="left",type="primary",width="stretch",shortcut="control+enter"):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()