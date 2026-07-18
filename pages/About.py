import streamlit as st

from components.theme import inject_global_css
from components.sidebar import render_sidebar
from components.cards import capability_card

st.set_page_config(page_title="BFCS Agent — About", page_icon="ℹ️", layout="wide")
inject_global_css()
render_sidebar(active="About BFCS Agent")

st.markdown("<span class='bfcs-badge'>Research Prototype</span>", unsafe_allow_html=True)
st.markdown("# About BFCS Agent")
st.markdown(
    "<p class='bfcs-subtitle'>Bayesian Federated Cervical Screening Agent</p>",
    unsafe_allow_html=True,
)
st.write("")

st.subheader("Project Overview")
st.markdown(
    "BFCS Agent is a clinical decision-support interface for cervical cytology review. "
    "It brings cell classification, segmentation, and explainability into a single, "
    "clinician-friendly workspace, with a Bayesian confidence layer designed for "
    "federated deployment across institutions."
)

st.subheader("Features")
feats = [
    ("🔬", "Multi-class Classification", "Normal / Other / Lesion / Cancer prediction with calibrated confidence."),
    ("🧩", "Segmentation Suite", "Background, cytoplasm, and nucleus masks with adjustable overlays."),
    ("🧠", "Explainable AI", "Grad-CAM heatmaps for transparent, auditable predictions."),
    ("📊", "Analytics Dashboard", "Full evaluation suite: ROC, PR, calibration, and confusion matrix."),
]
cols = st.columns(2)
for i, (icon, title, desc) in enumerate(feats):
    with cols[i % 2]:
        capability_card(icon, title, desc)
        st.write("")

st.subheader("Technologies Used")
st.markdown(
    "- **Frontend:** Streamlit, Plotly, Pillow, OpenCV\n"
    "- **Backend (to be connected):** model-agnostic inference API\n"
    "- **Architecture:** modular components (`components/`), utilities (`utils/`), "
    "multi-page Streamlit app\n"
)

st.subheader("Future Extensions")
st.markdown(
    "- Live federated training dashboard across partner institutions\n"
    "- Real-time model versioning and A/B evaluation\n"
    "- Integration with hospital PACS / LIS systems\n"
    "- Multi-language clinician-facing reports\n"
)

st.divider()
st.warning(
    "**BFCS Agent is a research prototype developed to assist cervical cytology review. "
    "It is not intended for clinical diagnosis or treatment decisions.**"
)
