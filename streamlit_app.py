import streamlit as st

st.set_page_config(
    page_title="实习摆渡人 - 县域大学生返乡实习智配平台",
    page_icon="⚓",
    layout="wide"
)

# Read the interactive HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render it full-width
st.components.v1.html(html_content, height=800, scrolling=True)