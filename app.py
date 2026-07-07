import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="US Beauty Brand Research",
    page_icon="💄",
    layout="centered",
)

# index.html 파일은 app.py와 같은 폴더에 있어야 합니다.
HTML_PATH = pathlib.Path(__file__).parent / "index.html"
html_content = HTML_PATH.read_text(encoding="utf-8")

# 원본 HTML/CSS/JS를 그대로 iframe에 렌더링합니다.
# height는 콘텐츠 길이에 맞춰 넉넉히 잡고, scrolling=True로 내부 스크롤을 허용합니다.
components.html(html_content, height=1400, scrolling=True)
