import streamlit as st 

def footer_home():
    logo_url = "https://png.pngtree.com/png-clipart/20250802/original/pngtree-creative-orange-gradient-letter-s-logo-vector-png-image_21556387.png"
    
    st.markdown(
        f"""
        <div style="display:flex; gap:2px; align-items:center; justify-content:center; margin-top:30px;">
            <p style="margin:0; font-weight:bold; color:white;">Created with ❤️ by</p>
            <img src="{logo_url}" style="height:35px;" alt="Logo">
        </div>
        """,
        unsafe_allow_html=True
    )
    
def footer_dashboard():
    logo_url = "https://png.pngtree.com/png-clipart/20250802/original/pngtree-creative-orange-gradient-letter-s-logo-vector-png-image_21556387.png"
    
    st.markdown(
        f"""
        <div style="display:flex; gap:2px; align-items:center; justify-content:center; margin-top:30px;">
            <p style="margin:0; font-weight:bold; color:black;">Created with ❤️ by</p>
            <img src="{logo_url}" style="height:35px;" alt="Logo">
        </div>
        """,
        unsafe_allow_html=True
    )