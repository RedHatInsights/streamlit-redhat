import streamlit as st


def login():
    st.button("Log in with Red Hat SSO", on_click=st.login, args=["stage"])
    st.stop()


if "is_logged_in" not in st.user.to_dict().keys():
    login()

user_info = st.user.to_dict()

if user_info.get("is_logged_in"):
    st.button("Log out", on_click=st.logout)
