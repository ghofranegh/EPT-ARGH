import io
import json

import streamlit as st
from PIL import Image

from components.theme import inject_global_css
from components.sidebar import render_sidebar
from components.cards import roi_card, download_card
from components.metrics import predicted_class_hero, confidence_gauge, probability_bars
from components.overlays import segmentation_viewer, before_after_slider, explainability_triptych
from utils.api import predict

st.set_page_config(page_title="BFCS Agent — Image Analysis", page_icon="🧬", layout="wide")
inject_global_css()
render_sidebar(active="Image Analysis")

st.markdown("<span class='bfcs-badge'>Research Prototype</span>", unsafe_allow_html=True)
st.markdown("# Image Analysis")
st.markdown(
    "<p class='bfcs-subtitle'>Upload a cytology image to run the full BFCS Agent analysis pipeline.</p>",
    unsafe_allow_html=True,
)
st.write("")

uploaded = st.file_uploader(
    "Upload a slide image", type=["png", "jpg", "jpeg", "tiff", "tif"],
    help="Accepted formats: PNG, JPG, JPEG, TIFF",
)

if uploaded is None:
    st.markdown(
        """
        <div class="bfcs-card" style="text-align:center; padding:3rem 1rem;">
            <div style="font-size:2rem;">🖼️</div>
            <div class="bfcs-card-title">No image uploaded yet</div>
            <div class="bfcs-card-desc">Upload a PNG, JPG, JPEG, or TIFF cytology slide to begin.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

image = Image.open(uploaded).convert("RGB")

with st.spinner("Running analysis pipeline…"):
    results = predict(image)  # backend placeholder — see utils/api.py

st.toast("Analysis complete ✅", icon="🧬")

left, right = st.columns([1, 1.3], gap="large")

# ------------------------------------------------------------- LEFT: IMAGE --
with left:
    st.markdown("### Original Image")
    st.image(image, use_container_width=True)
    st.caption(f"{uploaded.name} · {image.size[0]}×{image.size[1]}px")

# ---------------------------------------------------------- RIGHT: RESULTS --
with right:
    st.markdown("### Analysis Results")

    c1, c2 = st.columns([1, 1])
    with c1:
        predicted_class_hero(results["predicted_class"], results["confidence"])
    with c2:
        confidence_gauge(results["confidence"])

    st.progress(results["confidence"], text=f"Confidence: {results['confidence']*100:.1f}%")

    st.markdown("#### Class Probabilities")
    probability_bars(results["probabilities"], predicted_class=results["predicted_class"])

st.divider()

# ------------------------------------------------------------ SEGMENTATION --
st.markdown("## Segmentation")
masks = {
    "Overlay": results["segmentation"]["overlay"],
    "Background": results["segmentation"]["background"],
    "Cytoplasm": results["segmentation"]["cytoplasm"],
    "Nucleus": results["segmentation"]["nucleus"],
}
segmentation_viewer(image, masks)

with st.expander("🔀 Before / After comparison"):
    before_after_slider(image, results["segmentation"]["overlay"], key="seg_before_after")

st.divider()

# --------------------------------------------------------- EXPLAINABILITY ---
st.markdown("## Explainability")
explainability_triptych(
    original=image,
    heatmap=results["gradcam"]["heatmap"],
    overlay=results["gradcam"]["overlay"],
)

st.divider()

# --------------------------------------------------------------- ROI GRID ---
st.markdown("## Region of Interest")
roi_cols = st.columns(len(results["regions_of_interest"]))
for col, roi in zip(roi_cols, results["regions_of_interest"]):
    with col:
        roi_card(roi["id"], roi["predicted_class"], roi["confidence"], image=roi["image"])

st.divider()

# ------------------------------------------------------------- JSON OUTPUT --
st.markdown("## JSON Output")
json_payload = {
    "predicted_class": results["predicted_class"],
    "confidence": round(results["confidence"], 4),
    "probabilities": {k: round(v, 4) for k, v in results["probabilities"].items()},
    "segmentation": {k: "‹image›" for k in masks},
    "gradcam": "gradcam_overlay.png",
    "regions_of_interest": [
        {"id": r["id"], "predicted_class": r["predicted_class"], "confidence": round(r["confidence"], 4)}
        for r in results["regions_of_interest"]
    ],
}
with st.expander("View raw JSON", expanded=False):
    st.json(json_payload)

st.divider()

# ------------------------------------------------------------------ EXPORT --
st.markdown("## Download Results")
d1, d2, d3, d4 = st.columns(4)

json_bytes = json.dumps(json_payload, indent=2).encode("utf-8")


def _img_bytes(img):
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="PNG")
    return buf.getvalue()


with d1:
    download_card("JSON Report", "Full structured result payload.", json_bytes,
                  "bfcs_report.json", "application/json", key="dl_json")
with d2:
    download_card("Overlay Image", "Segmentation overlay on original.", _img_bytes(results["segmentation"]["overlay"]),
                  "overlay.png", "image/png", key="dl_overlay")
with d3:
    download_card("Segmentation Masks", "Nucleus mask (example export).", _img_bytes(results["segmentation"]["nucleus"]),
                  "nucleus_mask.png", "image/png", key="dl_masks")
with d4:
    download_card("Heatmap", "Grad-CAM explainability heatmap.", _img_bytes(results["gradcam"]["heatmap"]),
                  "heatmap.png", "image/png", key="dl_heatmap")
