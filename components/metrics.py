"""metrics.py — confidence gauge, probability bars, KPI tiles."""

import streamlit as st
import plotly.graph_objects as go

from components.theme import PALETTE


def confidence_gauge(confidence: float, height: int = 220):
    """Circular gauge for the model's confidence in its top prediction."""
    pct = round(confidence * 100, 1)
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=pct,
            number={"suffix": "%", "font": {"size": 34, "color": PALETTE["navy"]}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": PALETTE["gray_300"]},
                "bar": {"color": PALETTE["teal"]},
                "bgcolor": PALETTE["gray_100"],
                "borderwidth": 0,
                "steps": [
                    {"range": [0, 50], "color": "#FCEAEA"},
                    {"range": [50, 80], "color": "#FCF3E3"},
                    {"range": [80, 100], "color": "#E7F8F0"},
                ],
            },
        )
    )
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter"},
    )
    st.plotly_chart(fig, use_container_width=True)


def predicted_class_hero(predicted_class: str, confidence: float):
    st.markdown(
        f"""
        <div class="bfcs-hero-class">
            <div class="label">Predicted Class</div>
            <div class="value">{predicted_class}</div>
            <div style="font-size:0.85rem; opacity:0.85;">Confidence: {confidence*100:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def probability_bars(probabilities: dict, predicted_class: str = None):
    """probabilities: {"Normal": 0.05, "Other": 0.03, "Lesion": 0.11, "Cancer": ...}"""
    ordered = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    for label, value in ordered:
        is_pred = label == predicted_class
        fill_class = "bfcs-prob-fill" if is_pred else "bfcs-prob-fill-muted"
        weight = "700" if is_pred else "500"
        st.markdown(
            f"""
            <div class="bfcs-prob-row">
                <div class="bfcs-prob-label">
                    <span style="font-weight:{weight};">{label}{' ✓' if is_pred else ''}</span>
                    <span>{value*100:.1f}%</span>
                </div>
                <div class="bfcs-prob-track">
                    <div class="{fill_class}" style="width:{value*100:.2f}%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def kpi_tile(label: str, value: str, delta: str = None, help_text: str = None):
    st.markdown(
        f"""
        <div class="bfcs-card" style="text-align:center;">
            <div style="font-size:0.78rem; color:var(--text-soft); text-transform:uppercase;
                        letter-spacing:0.04em; font-weight:600;">{label}</div>
            <div style="font-size:1.8rem; font-weight:800; color:var(--navy); margin:0.15rem 0;">
                {value}
            </div>
            {f'<div style="font-size:0.78rem; color:var(--teal-dark); font-weight:600;">{delta}</div>' if delta else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )
    if help_text:
        st.caption(help_text)
