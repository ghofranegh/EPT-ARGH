import streamlit as st

from components.theme import inject_global_css
from components.sidebar import render_sidebar
from components.metrics import kpi_tile
from utils.visualization import (
    confusion_matrix_fig, roc_curve_fig, pr_curve_fig,
    reliability_diagram_fig, training_history_fig,
)

st.set_page_config(page_title="BFCS Agent — Model Performance", page_icon="📈", layout="wide")
inject_global_css()
render_sidebar(active="Model Performance")

st.markdown("<span class='bfcs-badge'>Research Prototype</span>", unsafe_allow_html=True)
st.markdown("# Model Performance")
st.markdown(
    "<p class='bfcs-subtitle'>Placeholder analytics — replace with real evaluation metrics once the "
    "backend is connected.</p>",
    unsafe_allow_html=True,
)
st.write("")

# ------------------------------------------------------------------- KPIs ---
kpis = [
    ("Accuracy", "0.912"), ("Precision", "0.887"), ("Recall", "0.901"), ("F1 Score", "0.894"),
    ("ROC-AUC", "0.947"), ("PR-AUC", "0.902"), ("MCC", "0.831"), ("Balanced Accuracy", "0.896"),
]
cols = st.columns(4)
for i, (label, value) in enumerate(kpis):
    with cols[i % 4]:
        kpi_tile(label, value)
        st.write("")

st.divider()

# ---------------------------------------------------------------- CHARTS ----
c1, c2 = st.columns(2)
with c1:
    st.markdown("#### Confusion Matrix")
    st.plotly_chart(confusion_matrix_fig(), use_container_width=True)
with c2:
    st.markdown("#### ROC Curve")
    st.plotly_chart(roc_curve_fig(), use_container_width=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown("#### Precision-Recall Curve")
    st.plotly_chart(pr_curve_fig(), use_container_width=True)
with c4:
    st.markdown("#### Reliability Diagram")
    st.plotly_chart(reliability_diagram_fig(), use_container_width=True)

st.markdown("#### Training History")
st.plotly_chart(training_history_fig(), use_container_width=True)

st.caption("All figures on this page are placeholders and will be replaced by live evaluation "
           "outputs once the inference backend is connected.")
