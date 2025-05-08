"""An example page with SSO integration.

https://docs.streamlit.io/develop/concepts/connections/authentication
"""

from streamlit_redhat.sso import user_info
import streamlit as st

st.markdown(f"Welcome! {user_info.name}")
with st.expander("[DEBUG] See the user JWT"):
    st.write(user_info)
