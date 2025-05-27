import streamlit as st
from streamlit_redhat.sso import user_info

if user_info:
    st.title(f"Hello, {user_info['name']}!")
    st.write(f"Your email is {user_info['email']}")
else:
    st.title("Hello, Guest!")
    st.write("Please log in to continue")
