import streamlit as st
from streamlit_redhat.sso import user_info
from streamlit_redhat.monitoring import streamlit_registry

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


if user_info:
    st.title(f"Hello, {user_info['name']}!")
    st.write(f"Your email is {user_info['email']}")
    USERS_COUNT.labels(name=user_info["name"]).inc()
else:
    st.title("Hello, Guest!")
    st.write("Please log in to continue")
