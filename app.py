import streamlit as st

from components.theme import inject_global_css
from components.sidebar import render_sidebar, render_logo
from components.cards import capability_card, status_card, workflow_row

st.set_page_config(
    page_title="BFCS Agent — Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_global_css()
render_sidebar(active="Dashboard")

# ---------------------------------------------------------------- HEADER ---
col_logo, col_head = st.columns([1, 6])
with col_logo:
    render_logo(80)
with col_head:
    st.markdown("<span class='bfcs-badge'>Research Prototype</span>", unsafe_allow_html=True)
    st.markdown("# BFCS Agent")
    st.markdown("### Bayesian Federated Cervical Screening Agent")
    st.markdown(
        "<p class='bfcs-subtitle'>AI-powered Clinical Decision Support System for Cervical Cytology</p>",
        unsafe_allow_html=True,
    )

st.write("")

# ------------------------------------------------------------ CAPABILITIES --
st.subheader("Platform Capabilities")
caps = [
    ("🔬", "Cervical Cell Classification", "Multi-class prediction across Normal, Other, Lesion, and Cancer categories."),
    ("🧩", "Cell Segmentation", "Pixel-level background, cytoplasm, and nucleus mask generation."),
    ("🧠", "Explainable AI", "Grad-CAM heatmaps overlaid on the original image for transparent reasoning."),
    ("📊", "Bayesian Confidence", "Calibrated probability outputs suited for clinical risk communication."),
    ("🌐", "Federated Learning Ready", "Architecture designed to train across institutions without sharing raw data."),
    ("🤖", "AI Medical Assistant", "Conversational support layer for interpreting results in context."),
]
cols = st.columns(3)
for i, (icon, title, desc) in enumerate(caps):
    with cols[i % 3]:
        capability_card(icon, title, desc)
        st.write("")

st.write("")

# ------------------------------------------------------------------ FLOW ---
st.subheader("Workflow")
workflow_row(["📤 Upload Image", "⚙️ Analysis", "🖼️ Visualization", "📋 Results", "📥 Export"])

st.write("")

# --------------------------------------------------------------- STATUS ----
st.subheader("System Status")
scols = st.columns(4)
with scols[0]:
    status_card("Backend Connection", ok=True, detail="Awaiting live endpoint")
with scols[1]:
    status_card("Segmentation Module", ok=True, detail="Mask generator ready")
with scols[2]:
    status_card("Explainability Module", ok=True, detail="Grad-CAM ready")
with scols[3]:
    status_card("Inference Engine", ok=False, detail="Model not yet connected")

st.write("")
st.info("👉 Head to **Image Analysis** in the sidebar to upload a slide and view a full result walkthrough.")
