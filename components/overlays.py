"""overlays.py — segmentation viewer (tabs + transparency), before/after slider,
explainability side-by-side. All inputs are PIL Images passed in from the backend
placeholder (utils/api.py) — no CV/ML logic lives here.
"""

import streamlit as st
import numpy as np
from PIL import Image


def _blend(base: Image.Image, overlay: Image.Image, alpha: float) -> Image.Image:
    base = base.convert("RGBA").resize(overlay.size)
    overlay = overlay.convert("RGBA")
    return Image.blend(base, overlay, alpha)


def segmentation_viewer(original: Image.Image, masks: dict):
    """masks: {"Overlay": PIL.Image, "Background": ..., "Cytoplasm": ..., "Nucleus": ...}"""
    tabs = st.tabs(list(masks.keys()))
    alpha = st.slider("Mask transparency", 0.0, 1.0, 0.55, 0.05, key="seg_alpha")
    fullscreen = st.toggle("🔍 Fullscreen view", key="seg_fullscreen")

    for tab, (name, mask_img) in zip(tabs, masks.items()):
        with tab:
            blended = _blend(original, mask_img, alpha)
            width = None if fullscreen else 620
            st.image(blended, caption=f"{name} mask over original", width=width,
                      use_container_width=fullscreen)


def before_after_slider(before: Image.Image, after: Image.Image, key: str):
    """Simple before/after comparison via a position slider (two synced crops)."""
    pos = st.slider("Compare: Original ↔ Processed", 0, 100, 50, key=key)
    w, h = before.size
    after_r = after.convert("RGB").resize((w, h))
    before_arr = np.array(before.convert("RGB"))
    after_arr = np.array(after_r)
    split = int(w * pos / 100)
    combined = before_arr.copy()
    combined[:, split:] = after_arr[:, split:]
    st.image(combined, use_container_width=True)
    st.caption(f"◀ Original ({100-pos}%)  ·  Processed ({pos}%) ▶")


def explainability_triptych(original: Image.Image, heatmap: Image.Image, overlay: Image.Image):
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Original Image**")
        st.image(original, use_container_width=True)
    with c2:
        st.markdown("**Heatmap (Grad-CAM)**")
        st.image(heatmap, use_container_width=True)
    with c3:
        st.markdown("**Overlay**")
        st.image(overlay, use_container_width=True)
