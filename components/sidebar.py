"""sidebar.py — shared sidebar: logo, navigation, version footer."""

import os
import streamlit as st

LOGO_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")

NAV_ITEMS = [
    {"icon": "🏠", "label": "Dashboard", "page": "app.py"},
    {"icon": "🧬", "label": "Image Analysis", "page": "pages/Image_Analysis.py"},
    {"icon": "📈", "label": "Model Performance", "page": "pages/Model_Performance.py"},
    {"icon": "ℹ️", "label": "About BFCS Agent", "page": "pages/About.py"},
]


def render_logo(width=120):
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=width)
    else:
        st.markdown(
            f"""
            <div style="
                width:{width}px; height:{width}px; margin:0 auto;
                border:2px dashed rgba(255,255,255,0.35); border-radius:16px;
                display:flex; align-items:center; justify-content:center;
                text-align:center; font-size:0.72rem; color:rgba(255,255,255,0.65);
                padding:0.4rem;">
                [ BFCS Agent Logo ]
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_sidebar(active: str = "Dashboard"):
    with st.sidebar:
        st.markdown("<div style='text-align:center; padding-top:0.5rem;'>", unsafe_allow_html=True)
        render_logo(90)
        st.markdown(
            "<div style='text-align:center; font-weight:800; font-size:1.05rem; margin-top:0.6rem;'>"
            "BFCS Agent</div>"
            "<div style='text-align:center; font-size:0.72rem; opacity:0.7; margin-bottom:1rem;'>"
            "Cervical Screening Agent</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.divider()

        for item in NAV_ITEMS:
            is_active = item["label"] == active
            prefix = "▸ " if is_active else ""
            if st.button(
                f"{item['icon']}  {prefix}{item['label']}",
                key=f"nav_{item['label']}",
                use_container_width=True,
            ):
                st.switch_page(item["page"])

        st.divider()
        st.markdown(
            "<div style='font-size:0.72rem; opacity:0.65;'>"
            "🔒 Local session · No PHI stored</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div style='position:fixed; bottom:1rem; font-size:0.72rem; opacity:0.6;'>"
            "Version 1.0</div>",
            unsafe_allow_html=True,
        )
