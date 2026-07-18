"""visualization.py — placeholder analytics charts (Plotly) for Model Performance.
Replace the synthetic arrays with real evaluation outputs when the backend is connected.
"""

import numpy as np
import plotly.graph_objects as go
import plotly.express as px

from components.theme import PALETTE

CLASSES = ["Normal", "Other", "Lesion", "Cancer"]


def confusion_matrix_fig(cm=None):
    if cm is None:
        rng = np.random.default_rng(7)
        cm = rng.integers(2, 40, size=(4, 4))
        np.fill_diagonal(cm, rng.integers(60, 140, size=4))
    fig = px.imshow(
        cm, x=CLASSES, y=CLASSES, text_auto=True, color_continuous_scale="Teal",
        labels=dict(x="Predicted", y="Actual", color="Count"),
    )
    fig.update_layout(margin=dict(l=10, r=10, t=30, b=10), height=380,
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig


def roc_curve_fig():
    fpr = np.linspace(0, 1, 50)
    tpr = np.clip(fpr ** 0.35 + np.random.default_rng(1).normal(0, 0.02, 50), 0, 1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name="Model",
                              line=dict(color=PALETTE["teal"], width=3)))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Chance",
                              line=dict(color=PALETTE["gray_300"], dash="dash")))
    fig.update_layout(xaxis_title="False Positive Rate", yaxis_title="True Positive Rate",
                       height=380, margin=dict(l=10, r=10, t=30, b=10),
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       legend=dict(orientation="h", y=-0.2))
    return fig


def pr_curve_fig():
    recall = np.linspace(0, 1, 50)
    precision = np.clip(1 - recall ** 1.8 + np.random.default_rng(2).normal(0, 0.02, 50), 0, 1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=recall, y=precision, mode="lines", name="Model",
                              line=dict(color=PALETTE["navy"], width=3), fill="tozeroy",
                              fillcolor="rgba(11,37,69,0.08)"))
    fig.update_layout(xaxis_title="Recall", yaxis_title="Precision",
                       height=380, margin=dict(l=10, r=10, t=30, b=10),
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig


def reliability_diagram_fig():
    bins = np.linspace(0.05, 0.95, 10)
    observed = np.clip(bins + np.random.default_rng(3).normal(0, 0.04, 10), 0, 1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=bins, y=observed, mode="lines+markers", name="Model",
                              line=dict(color=PALETTE["teal_dark"], width=3)))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Perfect calibration",
                              line=dict(color=PALETTE["gray_300"], dash="dash")))
    fig.update_layout(xaxis_title="Mean predicted probability", yaxis_title="Observed frequency",
                       height=380, margin=dict(l=10, r=10, t=30, b=10),
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       legend=dict(orientation="h", y=-0.2))
    return fig


def training_history_fig():
    epochs = np.arange(1, 31)
    rng = np.random.default_rng(4)
    train_loss = np.exp(-epochs / 10) + rng.normal(0, 0.01, 30) + 0.05
    val_loss = np.exp(-epochs / 12) + rng.normal(0, 0.015, 30) + 0.09
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=epochs, y=train_loss, mode="lines", name="Train loss",
                              line=dict(color=PALETTE["teal"], width=2.5)))
    fig.add_trace(go.Scatter(x=epochs, y=val_loss, mode="lines", name="Validation loss",
                              line=dict(color=PALETTE["navy"], width=2.5, dash="dot")))
    fig.update_layout(xaxis_title="Epoch", yaxis_title="Loss",
                       height=380, margin=dict(l=10, r=10, t=30, b=10),
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       legend=dict(orientation="h", y=-0.2))
    return fig
