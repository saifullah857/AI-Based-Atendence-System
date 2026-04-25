import streamlit as st 


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(
        f"""
        <div style="display:flex;flex-direction:column; align-items:center; justify-content:center; margin-bottem:30px; margin-top:10px;">
        <img src="{logo_url}" alt="Logo" height="100" ">
        <h1 style="text-align: center; color: #E0E3FF;">SNAP <br> CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(
        f"""
        <div style="display:flex;align-items:center; justify-content:center; gap:9px; ">
        <img src="{logo_url}" alt="Logo" height="85" ">
        <h1 style="text-align: left; color: #5865F2;">SNAP <br> CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )