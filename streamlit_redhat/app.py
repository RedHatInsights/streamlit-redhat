import streamlit as st
from streamlit_redhat.sso import user_info, login
from streamlit_redhat.monitoring import streamlit_registry
import streamlit_redhat.style as css

css.add_logo()

st.title("Welcome to Red Hat's Streamlit demo")

css.load_template("red-hat.css")

with st.sidebar:
    st.write("This is some text")
    st.button("A button")

from prometheus_client import Counter


registry = streamlit_registry()


@st.cache_resource
def get_users_count():
    return Counter(
        name="users_count",
        documentation="Number of users",
        labelnames=("name",),
        registry=registry,
    )


USERS_COUNT = get_users_count()


if user_info.get("is_logged_in"):
    st.write(f"Hello, {user_info['name']}!")
    st.write(f"Your email is {user_info['email']}")
    USERS_COUNT.labels(name=user_info["name"]).inc()
else:
    st.title("Hello, Guest!")
    st.write("Please log in to continue")
    login()
