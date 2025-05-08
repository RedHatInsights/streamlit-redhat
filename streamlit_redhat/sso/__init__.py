import streamlit as st

if not st.experimental_user.is_logged_in:
    st.button("Log in with Red Hat SSO", on_click=st.login, args=["stage"])
    st.stop()

st.button("Log out", on_click=st.logout)

user_info = st.experimental_user
