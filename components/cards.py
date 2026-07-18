"""cards.py — reusable card renderers used across pages."""

import streamlit as st


def capability_card(icon: str, title: str, desc: str):
    st.markdown(
        f"""
        <div class="bfcs-card">
            <div class="bfcs-card-icon">{icon}</div>
            <div class="bfcs-card-title">{title}</div>
            <div class="bfcs-card-desc">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def status_card(title: str, ok: bool, detail: str = ""):
    pill_class = "bfcs-pill-on" if ok else "bfcs-pill-off"
    dot_color = "#1FAA6D" if ok else "#DC4C4C"
    label = "Online" if ok else "Offline"
    st.markdown(
        f"""
        <div class="bfcs-card">
            <div class="bfcs-card-title" style="margin-bottom:0.5rem;">{title}</div>
            <span class="bfcs-pill {pill_class}">
                <span class="bfcs-dot" style="background:{dot_color};"></span> {label}
            </span>
            <div class="bfcs-card-desc" style="margin-top:0.5rem;">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def workflow_row(steps: list):
    cols = st.columns(len(steps) * 2 - 1)
    for i, step in enumerate(steps):
        col_idx = i * 2
        with cols[col_idx]:
            st.markdown(f"<div class='bfcs-step'>{step}</div>", unsafe_allow_html=True)
        if col_idx + 1 < len(cols):
            with cols[col_idx + 1]:
                st.markdown("<div class='bfcs-step-arrow'>→</div>", unsafe_allow_html=True)


def roi_card(region_id: str, predicted_class: str, confidence: float, image=None):
    st.markdown("<div class='bfcs-roi-card'>", unsafe_allow_html=True)
    if image is not None:
        st.image(image, use_container_width=True)
    st.markdown(
        f"""
        <div style="font-weight:700; color:var(--navy); font-size:0.85rem; margin-top:0.4rem;">
            {region_id}
        </div>
        <div style="font-size:0.78rem; color:var(--text-soft);">
            {predicted_class} · {confidence*100:.1f}%
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


def download_card(title: str, desc: str, data: bytes, file_name: str, mime: str, key: str):
    st.markdown(
        f"""
        <div class="bfcs-download">
            <div class="bfcs-card-title" style="font-size:0.92rem;">{title}</div>
            <div class="bfcs-card-desc" style="margin-bottom:0.6rem;">{desc}</div>
        """,
        unsafe_allow_html=True,
    )
    st.download_button(
        "⬇ Download",
        data=data,
        file_name=file_name,
        mime=mime,
        key=key,
        use_container_width=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
