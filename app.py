import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Adithya & Dhivya",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "anniversary.html"

html = html_path.read_text(encoding="utf-8")

# Render the existing HTML/CSS/JavaScript anniversary website inside Streamlit.
components.html(
    html,
    height=1800,
    scrolling=True,
)
