import streamlit as st

st.set_page_config(
    page_title="实习摆渡人 - 县域大学生返乡实习智配平台",
    page_icon="⛴",
    layout="wide"
)

# 隐藏 Streamlit 的菜单栏、页脚和顶栏
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {margin-top: -80px;}
.stDeployButton {display: none !important;}
section[data-testid="stSidebar"] {display: none !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read the interactive HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 全屏渲染
st.components.v1.html(html_content, height=900, scrolling=True)
