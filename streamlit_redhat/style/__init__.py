import streamlit as st


def add_logo():
    """Display the Red Hat logo and icon in the Streamlit app."""
    # TODO: add logos for dark mode when https://github.com/streamlit/streamlit/issues/5009 is fixed.
    HORIZONTAL = "streamlit_redhat/style/assets/Logo-Red_Hat-A-Standard-RGB.svg"
    ICON = "streamlit_redhat/style/assets/Logo-Red_Hat-Hat_icon-Standard-RGB.svg"
    st.logo(HORIZONTAL, icon_image=ICON)

def load_template(template: str):
    """Load a CSS template from the specified file.

    Args:
        template (str): The name of the CSS template file to load.
    """
    with open(f"streamlit_redhat/style/templates/{template}", encoding="utf-8") as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def centered_markdown(content: str, color="black"):
    """Display centered markdown content.

    Args:
        content (str): The markdown content to display.
        color (str): The color of the text (default is "black").
    """
    st.markdown(
        f"<p style='text-align: center; color: {color};'>{content}</p>",
        unsafe_allow_html=True
    )  

def hline():
    """Display a horizontal line."""
    st.markdown("---")
