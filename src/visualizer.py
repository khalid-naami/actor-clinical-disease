"""Interactive Clinical Visualizations Engine using Plotly.

Generates macronutrient distribution donuts, biomarker radar charts,
exercise volume gauges, multi-disease epidemiological comparisons, and risk staging charts.
"""

from typing import Dict, List, Any
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

CHART_THEME = {
    "paper_bgcolor": "rgba(15, 23, 42, 0.0)",
    "plot_bgcolor": "rgba(15, 23, 42, 0.0)",
    "font_color": "#e2e8f0",
    "grid_color": "rgba(148, 163, 184, 0.15)"
}

def create_macronutrient_donut(macros: Dict[str, Any], diet_name: str) -> go.Figure:
    """Creates an interactive clinical macronutrient distribution donut chart."""
    labels = ["Carbohydrates", "Proteins", "Healthy Fats"]
    values = []
    
    for k in labels:
        val = macros.get(k, 33)
        if isinstance(val, str):
            # Extract first number if range or text
            import re
            nums = re.findall(r'\d+', val)
            val = int(nums[0]) if nums else 20
        values.append(val)
        
    colors = ["#38bdf8", "#34d399", "#f59e0b"]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.55,
        marker=dict(colors=colors, line=dict(color="#0f172a", width=2)),
        textinfo="label+percent",
        textfont=dict(size=13, color="#ffffff"),
        hoverinfo="label+value+percent"
    )])
    
    fig.update_layout(
        title=dict(text=f"<b>Therapeutic Macronutrient Ratio</b><br><span style='font-size:12px; color:#94a3b8;'>{diet_name}</span>", font=dict(color="#f8fafc", size=15)),
        paper_bgcolor=CHART_THEME["paper_bgcolor"],
        plot_bgcolor=CHART_THEME["plot_bgcolor"],
        font=dict(color=CHART_THEME["font_color"]),
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
        height=320
    )
    return fig

def create_risk_score_gauge(score: int, title: str, status_text: str = "") -> go.Figure:
    """Creates a clinical indicator gauge for health risk or longevity index."""
    if score >= 80: bar_color = "#10b981"
    elif score >= 60: bar_color = "#38bdf8"
    elif score >= 40: bar_color = "#eab308"
    elif score >= 20: bar_color = "#f97316"
    else: bar_color = "#ef4444"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': f"<b>{title}</b><br><span style='font-size:13px; color:#94a3b8;'>{status_text}</span>", 'font': {'size': 16, 'color': '#f8fafc'}},
        number={'suffix': "%", 'font': {'size': 36, 'color': '#ffffff'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94a3b8"},
            'bar': {'color': bar_color, 'thickness': 0.3},
            'bgcolor': "rgba(30, 41, 59, 0.6)",
            'borderwidth': 1,
            'bordercolor': "rgba(148, 163, 184, 0.3)",
            'steps': [
                {'range': [0, 30], 'color': "rgba(239, 68, 68, 0.2)"},
                {'range': [30, 60], 'color': "rgba(234, 179, 8, 0.2)"},
                {'range': [60, 100], 'color': "rgba(16, 185, 129, 0.2)"}
            ],
            'threshold': {
                'line': {'color': "#ffffff", 'width': 3},
                'thickness': 0.8,
                'value': score
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor=CHART_THEME["paper_bgcolor"],
        plot_bgcolor=CHART_THEME["plot_bgcolor"],
        font=dict(color=CHART_THEME["font_color"]),
        margin=dict(l=30, r=30, t=60, b=20),
        height=280
    )
    return fig

def create_global_epidemiology_bar() -> go.Figure:
    """Comparative bar chart of global prevalence and annual mortality across 7 diseases."""
    diseases = [
        "Cardiovascular / CAD",
        "Hypertension",
        "Chronic Kidney Disease",
        "Type 2 Diabetes",
        "COPD / Respiratory",
        "Alzheimer's / Dementia",
        "Oncology (5-Yr Prevalent)"
    ]
    prevalence_millions = [620, 1280, 850, 537, 392, 55, 50.5]
    mortality_millions = [19.8, 10.8, 3.1, 6.7, 3.23, 1.9, 10.0]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=diseases,
        y=prevalence_millions,
        name="Global Prevalent Population (Millions)",
        marker_color="#38bdf8",
        opacity=0.85
    ))
    fig.add_trace(go.Bar(
        x=diseases,
        y=mortality_millions,
        name="Annual Mortality (Millions/Year)",
        marker_color="#ef4444",
        opacity=0.85
    ))

    fig.update_layout(
        title=dict(text="<b>Global Disease Burden: Prevalent Population vs Annual Mortality</b>", font=dict(color="#f8fafc", size=16)),
        barmode='group',
        paper_bgcolor=CHART_THEME["paper_bgcolor"],
        plot_bgcolor=CHART_THEME["plot_bgcolor"],
        font=dict(color=CHART_THEME["font_color"]),
        xaxis=dict(gridcolor=CHART_THEME["grid_color"], tickangle=-20),
        yaxis=dict(title="Millions of Individuals", gridcolor=CHART_THEME["grid_color"], type="log"),
        margin=dict(l=40, r=20, t=50, b=60),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=380
    )
    return fig

def create_exercise_volume_gauge(target_min: int = 150, current_min: int = 120) -> go.Figure:
    """Gauge showing weekly exercise minutes against clinical guideline targets."""
    pct = min(100, int((current_min / target_min) * 100))
    bar_color = "#10b981" if current_min >= target_min else ("#38bdf8" if current_min >= 90 else "#f59e0b")

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=current_min,
        delta={'reference': target_min, 'increasing': {'color': "#10b981"}, 'decreasing': {'color': "#ef4444"}},
        title={'text': f"<b>Weekly Physical Activity Volume</b><br><span style='font-size:12px; color:#94a3b8;'>Clinical Guideline Target: {target_min} min/week</span>", 'font': {'size': 15, 'color': '#f8fafc'}},
        number={'suffix': " min", 'font': {'size': 32, 'color': '#ffffff'}},
        gauge={
            'axis': {'range': [0, max(300, current_min + 50)], 'tickcolor': "#94a3b8"},
            'bar': {'color': bar_color, 'thickness': 0.3},
            'bgcolor': "rgba(30, 41, 59, 0.6)",
            'steps': [
                {'range': [0, 75], 'color': "rgba(239, 68, 68, 0.2)"},
                {'range': [75, 150], 'color': "rgba(234, 179, 8, 0.2)"},
                {'range': [150, 300], 'color': "rgba(16, 185, 129, 0.2)"}
            ],
            'threshold': {
                'line': {'color': "#34d399", 'width': 3},
                'thickness': 0.8,
                'value': target_min
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor=CHART_THEME["paper_bgcolor"],
        plot_bgcolor=CHART_THEME["plot_bgcolor"],
        font=dict(color=CHART_THEME["font_color"]),
        margin=dict(l=30, r=30, t=60, b=20),
        height=280
    )
    return fig
