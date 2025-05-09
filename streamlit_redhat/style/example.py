import streamlit as st  
import streamlit_redhat.style as css

css.add_logo()

st.title("Welcome to Red Hat's Streamlit demo")

css.hline()
css.centered_markdown("This is a demo showing how to apply custom css to your app")
css.hline()

css.load_template("red-hat.css")

with st.sidebar:
    st.write("This is some text")
    st.button("A button")
