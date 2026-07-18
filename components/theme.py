"""
theme.py — shared visual identity for BFCS Agent.

Palette:
  --bfcs-navy      #0B2545  (primary dark blue)
  --bfcs-teal      #14B8A6  (accent / interactive)
  --bfcs-teal-dark #0D9488
  --bfcs-white     #FFFFFF
  --bfcs-gray-50   #F7F9FB  (page background)
  --bfcs-gray-100  #EEF2F6  (card background)
  --bfcs-gray-300  #D8E0E9  (borders)
  --bfcs-text      #1B2A3A
  --bfcs-text-soft #5B6B7C
"""

import streamlit as st

PALETTE = {
    "navy": "#0B2545",
    "teal": "#14B8A6",
    "teal_dark": "#0D9488",
    "white": "#FFFFFF",
    "gray_50": "#F7F9FB",
    "gray_100": "#EEF2F6",
    "gray_300": "#D8E0E9",
    "text": "#1B2A3A",
    "text_soft": "#5B6B7C",
    "danger": "#DC4C4C",
    "warning": "#E8A33D",
    "success": "#1FAA6D",
}


def inject_global_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, [class*="css"]  {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}

        :root {{
            --navy: {PALETTE['navy']};
            --teal: {PALETTE['teal']};
            --teal-dark: {PALETTE['teal_dark']};
            --gray-50: {PALETTE['gray_50']};
            --gray-100: {PALETTE['gray_100']};
            --gray-300: {PALETTE['gray_300']};
            --text: {PALETTE['text']};
            --text-soft: {PALETTE['text_soft']};
        }}

        .stApp {{
            background: var(--gray-50);
        }}

        /* Hide default multipage nav — we render our own in sidebar.py */
        [data-testid="stSidebarNav"] {{ display: none; }}

        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, var(--navy) 0%, #0F2E52 100%);
            border-right: 1px solid #12305a;
        }}
        section[data-testid="stSidebar"] * {{
            color: #E7EEF6 !important;
        }}
        section[data-testid="stSidebar"] hr {{
            border-color: rgba(255,255,255,0.12);
        }}

        /* Sidebar nav buttons */
        section[data-testid="stSidebar"] .stButton button {{
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.10);
            color: #E7EEF6 !important;
            text-align: left;
            border-radius: 10px;
            padding: 0.55rem 0.9rem;
            width: 100%;
            font-weight: 500;
            transition: all 0.15s ease;
        }}
        section[data-testid="stSidebar"] .stButton button:hover {{
            background: var(--teal);
            border-color: var(--teal);
            color: #06201c !important;
        }}
        section[data-testid="stSidebar"] .stButton button:focus:not(:active) {{
            outline: 2px solid var(--teal);
        }}

        /* Headings */
        h1, h2, h3 {{ color: var(--navy); font-weight: 800; letter-spacing: -0.02em; }}

        /* Badge */
        .bfcs-badge {{
            display: inline-block;
            background: var(--gray-100);
            color: var(--teal-dark);
            border: 1px solid var(--teal);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            margin-bottom: 0.4rem;
        }}

        .bfcs-subtitle {{
            color: var(--text-soft);
            font-size: 1.05rem;
            margin-top: -0.5rem;
        }}

        /* Generic card */
        .bfcs-card {{
            background: #FFFFFF;
            border: 1px solid var(--gray-300);
            border-radius: 16px;
            padding: 1.25rem 1.4rem;
            box-shadow: 0 1px 2px rgba(16, 42, 67, 0.04), 0 8px 24px rgba(16, 42, 67, 0.04);
            height: 100%;
        }}
        .bfcs-card:hover {{
            border-color: var(--teal);
            box-shadow: 0 4px 10px rgba(20, 184, 166, 0.10), 0 12px 28px rgba(16, 42, 67, 0.06);
        }}

        .bfcs-card-title {{
            font-weight: 700;
            color: var(--navy);
            font-size: 1.02rem;
            margin-bottom: 0.25rem;
        }}
        .bfcs-card-desc {{
            color: var(--text-soft);
            font-size: 0.88rem;
            line-height: 1.4rem;
        }}
        .bfcs-card-icon {{
            font-size: 1.6rem;
            margin-bottom: 0.5rem;
        }}

        /* Status pill */
        .bfcs-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.78rem;
            font-weight: 600;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
        }}
        .bfcs-pill-on {{ background: #E7F8F0; color: {PALETTE['success']}; }}
        .bfcs-pill-off {{ background: #FCEAEA; color: {PALETTE['danger']}; }}
        .bfcs-pill-warn {{ background: #FCF3E3; color: {PALETTE['warning']}; }}

        .bfcs-dot {{
            width: 8px; height: 8px; border-radius: 50%; display: inline-block;
        }}

        /* Predicted class hero card */
        .bfcs-hero-class {{
            background: linear-gradient(135deg, var(--navy), #12406f);
            color: white;
            border-radius: 18px;
            padding: 1.6rem 1.8rem;
            text-align: center;
        }}
        .bfcs-hero-class .label {{
            font-size: 0.8rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            opacity: 0.75;
        }}
        .bfcs-hero-class .value {{
            font-size: 2.4rem;
            font-weight: 800;
            margin: 0.15rem 0;
        }}

        /* Probability bar */
        .bfcs-prob-row {{ margin-bottom: 0.55rem; }}
        .bfcs-prob-label {{
            display: flex; justify-content: space-between;
            font-size: 0.85rem; font-weight: 600; color: var(--text);
            margin-bottom: 0.2rem;
        }}
        .bfcs-prob-track {{
            width: 100%; height: 10px; background: var(--gray-100);
            border-radius: 999px; overflow: hidden;
        }}
        .bfcs-prob-fill {{
            height: 100%; border-radius: 999px;
            background: linear-gradient(90deg, var(--teal-dark), var(--teal));
        }}
        .bfcs-prob-fill-muted {{
            height: 100%; border-radius: 999px; background: var(--gray-300);
        }}

        /* Workflow step */
        .bfcs-step {{
            background: white;
            border: 1px dashed var(--gray-300);
            border-radius: 14px;
            padding: 0.9rem;
            text-align: center;
            font-weight: 600;
            color: var(--navy);
            font-size: 0.85rem;
        }}
        .bfcs-step-arrow {{
            text-align: center;
            color: var(--teal);
            font-size: 1.3rem;
            font-weight: 800;
        }}

        /* Region of interest card */
        .bfcs-roi-card {{
            background: white; border: 1px solid var(--gray-300); border-radius: 12px;
            padding: 0.6rem; text-align: center;
        }}

        /* Download card */
        .bfcs-download {{
            border: 1px solid var(--gray-300);
            background: white;
            border-radius: 12px;
            padding: 0.9rem 1rem;
        }}

        footer {{visibility: hidden;}}
        #MainMenu {{visibility: hidden;}}
        </style>
        """,
        unsafe_allow_html=True,
    )
