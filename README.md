# BFCS Agent — Streamlit Frontend

UI-only implementation. No ML models are implemented — `utils/api.py::predict()`
is a mock backend placeholder that returns the exact schema the UI expects.

## Run

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

## Connect a real backend

Edit `utils/api.py`. Keep the return schema identical (see the docstring at
the top of the file) and every page keeps working unchanged.

## Add your logo

Drop a file at `assets/logo.png` — it will automatically replace the
`[ BFCS Agent Logo ]` placeholder in the sidebar and dashboard header.

## Structure

```
streamlit_app/
├── app.py                      # Dashboard (home) page
├── pages/
│   ├── 2_🧬_Image_Analysis.py
│   ├── 3_📈_Model_Performance.py
│   └── 4_ℹ️_About.py
├── components/                 # sidebar, cards, metrics, overlays, theme (CSS)
├── utils/                      # api.py (backend placeholder), visualization.py
├── assets/                     # logo.png, banner.png (optional)
└── outputs/                    # runtime-generated exports land here
```
