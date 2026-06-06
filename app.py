import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import psycopg2
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

try:
    DB_URL = st.secrets["DB_URL"]
except Exception:
    DB_URL = os.getenv("DB_URL")

def run_query(query):
    try:
        parsed = urllib.parse.urlparse(DB_URL)
        st.write("Host:", parsed.hostname)
        st.write("Port:", parsed.port)
        st.write("DB:", parsed.path.lstrip("/"))
        st.write("User:", parsed.username)
        st.write("Password length:", len(urllib.parse.unquote(parsed.password)) if parsed.password else 0)
        conn = psycopg2.connect(
            host=parsed.hostname,
            port=parsed.port or 5432,
            database=parsed.path.lstrip("/"),
            user=parsed.username,
            password=urllib.parse.unquote(parsed.password),
            sslmode="require"
        )
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        st.stop()

st.set_page_config(
    page_title="P2P Lending Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #FAFAF8;
    color: #1a1a1a;
}

[data-testid="stAppViewContainer"] {
    background-color: #FAFAF8;
}

[data-testid="stSidebar"] {
    background-color: #1C1C2E;
    border-right: none;
}

[data-testid="stSidebar"] * {
    color: #E8E8F0 !important;
}

[data-testid="stSidebar"] .stRadio > label {
    color: #A0A0B8 !important;
    font-size: 13px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 500;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: transparent;
    border: 1px solid #2E2E45;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 6px;
    transition: all 0.2s ease;
    color: #C0C0D8 !important;
    font-size: 14px;
    font-weight: 400;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: #2E2E45;
    border-color: #7C6AF7;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-baseweb="radio"] {
    background: #2E2E45;
    border-color: #7C6AF7;
    color: #ffffff !important;
}

.sidebar-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #ffffff;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
}

.sidebar-sub {
    font-size: 12px;
    color: #6B6B8A;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 32px;
}

.sidebar-divider {
    border: none;
    border-top: 1px solid #2E2E45;
    margin: 20px 0;
}

.sidebar-label {
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #6B6B8A;
    margin-bottom: 12px;
    font-weight: 500;
}

.page-header {
    padding: 40px 0 8px 0;
}

.page-title {
    font-family: 'DM Serif Display', serif;
    font-size: 42px;
    font-weight: 400;
    color: #0F0F1A;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 8px;
}

.page-subtitle {
    font-size: 16px;
    color: #6B6B8A;
    font-weight: 300;
    letter-spacing: 0.01em;
    margin-bottom: 36px;
}

.accent-bar {
    width: 48px;
    height: 4px;
    background: linear-gradient(90deg, #7C6AF7, #F76A8A);
    border-radius: 2px;
    margin-bottom: 20px;
}

.kpi-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 24px 24px 20px 24px;
    border: 1px solid #EEEEF4;
    position: relative;
    overflow: hidden;
}

.kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: linear-gradient(180deg, #7C6AF7, #F76A8A);
    border-radius: 16px 0 0 16px;
}

.kpi-label {
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #9898B0;
    font-weight: 500;
    margin-bottom: 10px;
}

.kpi-value {
    font-family: 'DM Serif Display', serif;
    font-size: 32px;
    color: #0F0F1A;
    letter-spacing: -0.02em;
    line-height: 1;
}

.kpi-sub {
    font-size: 12px;
    color: #B0B0C8;
    margin-top: 6px;
}

.section-title {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4A4A6A;
    margin-bottom: 16px;
    margin-top: 32px;
}

.chart-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #EEEEF4;
}

div[data-testid="stMetricValue"] {
    font-family: 'DM Serif Display', serif;
    font-size: 32px;
    color: #0F0F1A;
}

div[data-testid="stMetricLabel"] {
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #9898B0;
}

.stDataFrame {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #EEEEF4;
}

.divider {
    border: none;
    border-top: 1px solid #EEEEF4;
    margin: 32px 0;
}

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

CHART_COLORS = {
    "primary":   "#7C6AF7",
    "secondary": "#F76A8A",
    "tertiary":  "#4ECDC4",
    "warning":   "#FFB347",
    "success":   "#6BCB77",
    "neutral":   "#C0C0D0",
}

PALETTE_SEQ  = ["#7C6AF7","#9B8DF9","#BAB0FB","#D8D3FD","#F0EEFF"]
PALETTE_DIV  = ["#F76A8A","#FA9BAD","#FCC8D1","#D8D3FD","#BAB0FB","#7C6AF7"]

PLOTLY_BASE = dict(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#ffffff",
    font_family="DM Sans",
    font_color="#1a1a1a",
    margin=dict(l=16, r=16, t=24, b=80),
    xaxis=dict(
        showgrid=True,
        gridcolor="#EEEEF4",
        zeroline=False,
        tickfont=dict(color="#4A4A6A", size=12),
        tickangle=-35,
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="#EEEEF4",
        zeroline=False,
        tickfont=dict(color="#4A4A6A", size=12),
    ),
)

def apply_base(fig, x_vals=None):
    fig.update_layout(**PLOTLY_BASE)
    if x_vals is not None:
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=x_vals[::3],
                ticktext=x_vals[::3],
                tickangle=-35,
                tickfont=dict(color="#4A4A6A", size=12),
                gridcolor="#EEEEF4",
            )
        )
    return fig

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">P2P Lending</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Analytics Platform</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        label="",
        options=[
            "Platform Overview",
            "Borrower Risk Analysis",
            "Lender Performance",
            "Repayment Health"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    st.markdown("""
        <div style="font-size:11px; color:#4A4A6A; line-height:1.8">
            <div style="margin-bottom:4px">300 Users</div>
            <div style="margin-bottom:4px">300 Loan Applications</div>
            <div style="margin-bottom:4px">150 Borrowers</div>
            <div style="margin-bottom:4px">150 Lenders</div>
            <div style="margin-bottom:16px">Live Supabase PostgreSQL</div>
        </div>
    """, unsafe_allow_html=True)


# ── PAGE 1: PLATFORM OVERVIEW ────────────────────────────────────────────────
if page == "Platform Overview":

    st.markdown("""
        <div class="page-header">
            <div class="accent-bar"></div>
            <div class="page-title">Platform Overview</div>
            <div class="page-subtitle">Monthly loan activity, approval trends, and platform-wide health metrics</div>
        </div>
    """, unsafe_allow_html=True)

    df = run_query("SELECT * FROM vw_platform_overview ORDER BY month")
    df["month"] = pd.to_datetime(df["month"])
    df["month_label"] = df["month"].dt.strftime("%b %Y")

    total_loans     = int(df["total_loans"].sum())
    total_volume    = float(df["total_loan_volume"].sum())
    avg_approval    = float(df["approval_rate_pct"].mean())
    avg_interest    = float(df["avg_interest_rate"].mean())
    total_disputes  = int(df["total_disputes"].sum())

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, label, value, sub in [
        (c1, "Total Loans", f"{total_loans:,}", "across all months"),
        (c2, "Loan Volume", f"${total_volume:,.0f}", "total disbursed"),
        (c3, "Avg Approval Rate", f"{avg_approval:.1f}%", "of applications"),
        (c4, "Avg Interest Rate", f"{avg_interest:.2f}%", "across portfolio"),
        (c5, "Total Disputes", f"{total_disputes:,}", "logged on platform"),
    ]:
        col.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Monthly Loan Volume</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Bar(
            x=df["month_label"], y=df["total_loan_volume"].astype(float),
            marker=dict(
                color=df["total_loan_volume"].astype(float),
                colorscale=[[0,"#D8D3FD"],[1,"#7C6AF7"]],
                showscale=False
            )
        ))
        apply_base(fig)
        fig.update_layout(
    xaxis_title="",
    yaxis_title="Volume ($)",
    xaxis=dict(
        tickmode="array",
        tickvals=df["month_label"].tolist()[::3],
        ticktext=df["month_label"].tolist()[::3],
        tickangle=-35,
        tickfont=dict(color="#4A4A6A", size=12),
        gridcolor="#EEEEF4",
    )
)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Approval Rate Trend</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df["month_label"],
            y=df["approval_rate_pct"].astype(float),
            mode="lines+markers",
            line=dict(color="#7C6AF7", width=3),
            marker=dict(color="#7C6AF7", size=7),
            fill="tozeroy",
            fillcolor="rgba(124,106,247,0.08)"
        ))
        apply_base(fig)
        fig.update_layout(
    yaxis_range=[0,100],
    yaxis_title="Approval Rate (%)",
    xaxis=dict(
        tickmode="array",
        tickvals=df["month_label"].tolist()[::3],
        ticktext=df["month_label"].tolist()[::3],
        tickangle=-35,
        tickfont=dict(color="#4A4A6A", size=12),
        gridcolor="#EEEEF4",
    )
)
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Application Status Breakdown</div>', unsafe_allow_html=True)
        status_totals = {
            "Approved":     int(df["approved"].sum()),
            "Rejected":     int(df["rejected"].sum()),
            "Pending":      int(df["pending"].sum()),
            "Under Review": int(df["under_review"].sum()),
        }
        fig = go.Figure(go.Pie(
            labels=list(status_totals.keys()),
            values=list(status_totals.values()),
            hole=0.55,
            marker_colors=["#7C6AF7","#F76A8A","#FFB347","#4ECDC4"],
            textinfo="percent+label",
            textfont_size=13,
        ))
        apply_base(fig)
        fig.update_layout(showlegend=False, margin=dict(l=16,r=16,t=16,b=16))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Loans vs Disputes by Month</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["month_label"], y=df["total_loans"],
            name="Total Loans",
            marker_color="#BAB0FB"
        ))
        fig.add_trace(go.Scatter(
            x=df["month_label"], y=df["total_disputes"],
            name="Disputes",
            mode="lines+markers",
            line=dict(color="#F76A8A", width=2.5),
            marker=dict(size=6)
        ))
        apply_base(fig, x_vals=df["month_label"].tolist())
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
            yaxis_title="Count"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Monthly Breakdown</div>', unsafe_allow_html=True)
    display_df = df[[
        "month_label","total_loans","total_loan_volume",
        "avg_loan_amount","avg_interest_rate",
        "approved","rejected","approval_rate_pct","total_disputes"
    ]].copy()
    display_df.columns = [
        "Month","Loans","Volume ($)","Avg Amount ($)",
        "Avg Rate (%)","Approved","Rejected","Approval Rate (%)","Disputes"
    ]
    st.dataframe(display_df, use_container_width=True, hide_index=True)


# ── PAGE 2: BORROWER RISK ─────────────────────────────────────────────────────
elif page == "Borrower Risk Analysis":

    st.markdown("""
        <div class="page-header">
            <div class="accent-bar"></div>
            <div class="page-title">Borrower Risk Analysis</div>
            <div class="page-subtitle">Loan-to-value ratios, rejection rates, dispute counts and credit behaviour across all borrowers</div>
        </div>
    """, unsafe_allow_html=True)

    df = run_query("SELECT * FROM vw_borrower_risk ORDER BY total_loans DESC")

    avg_ltv       = float(df["avg_loan_to_value_ratio"].mean())
    avg_rejection = float(df["rejection_rate_pct"].mean())
    avg_disputes  = float(df["total_disputes"].mean())
    avg_rating    = float(df["avg_rating"].dropna().mean())

    c1, c2, c3, c4 = st.columns(4)
    for col, label, value, sub in [
        (c1, "Avg Loan-to-Value", f"{avg_ltv:.2f}x", "across borrowers"),
        (c2, "Avg Rejection Rate", f"{avg_rejection:.1f}%", "of applications"),
        (c3, "Avg Disputes", f"{avg_disputes:.1f}", "per borrower"),
        (c4, "Avg Borrower Rating", f"{avg_rating:.2f}", "out of 5"),
    ]:
        col.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Top 20 Borrowers by Avg Loan Amount</div>', unsafe_allow_html=True)
        top20 = df.nlargest(20, "avg_loan_amount")
        fig = go.Figure(go.Bar(
            x=top20["avg_loan_amount"].astype(float),
            y=top20["borrower_name"],
            orientation="h",
            marker=dict(
                color=top20["avg_loan_amount"].astype(float),
                colorscale=[[0,"#D8D3FD"],[1,"#7C6AF7"]],
                showscale=False
            )
        ))
        apply_base(fig)
        fig.update_layout(
            yaxis=dict(autorange="reversed"),
            xaxis_title="Avg Loan Amount ($)",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Loan-to-Value Distribution</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Histogram(
            x=df["avg_loan_to_value_ratio"].astype(float),
            nbinsx=20,
            marker_color="#7C6AF7",
            opacity=0.85
        ))
        apply_base(fig)
        fig.update_layout(xaxis_title="LTV Ratio", yaxis_title="Borrower Count")
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Rejection Rate vs Dispute Count</div>', unsafe_allow_html=True)
        fig = px.scatter(
            df,
            x="rejection_rate_pct",
            y="total_disputes",
            hover_name="borrower_name",
            size="total_loans",
            color="avg_rating",
            color_continuous_scale=["#F76A8A","#FFB347","#6BCB77"],
            labels={
                "rejection_rate_pct": "Rejection Rate (%)",
                "total_disputes": "Total Disputes",
                "avg_rating": "Avg Rating"
            }
        )
        apply_base(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Collateral Coverage Distribution</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Histogram(
            x=df["avg_collateral_coverage_pct"].astype(float),
            nbinsx=20,
            marker_color="#4ECDC4",
            opacity=0.85
        ))
        apply_base(fig)
        fig.update_layout(xaxis_title="Collateral Coverage (%)", yaxis_title="Borrower Count")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Full Borrower Risk Table</div>', unsafe_allow_html=True)
    risk_df = df[[
        "borrower_name","total_loans","avg_loan_amount",
        "avg_loan_to_value_ratio","avg_collateral_coverage_pct",
        "total_disputes","rejection_rate_pct","avg_rating"
    ]].copy()
    risk_df.columns = [
        "Borrower","Loans","Avg Loan ($)","LTV Ratio",
        "Collateral Cover (%)","Disputes","Rejection Rate (%)","Avg Rating"
    ]
    st.dataframe(risk_df, use_container_width=True, hide_index=True)


# ── PAGE 3: LENDER PERFORMANCE ───────────────────────────────────────────────
elif page == "Lender Performance":

    st.markdown("""
        <div class="page-header">
            <div class="accent-bar"></div>
            <div class="page-title">Lender Performance</div>
            <div class="page-subtitle">Investment capacity, fund statuses, ratings and portfolio returns across all lenders</div>
        </div>
    """, unsafe_allow_html=True)

    df = run_query("SELECT * FROM vw_lender_performance ORDER BY total_amount_lent DESC NULLS LAST")

    total_lent      = float(df["total_amount_lent"].sum())
    avg_rating      = float(df["avg_rating"].dropna().mean())
    total_completed = int(df["completed_fundings"].sum())
    total_cancelled = int(df["cancelled_fundings"].sum())

    c1, c2, c3, c4 = st.columns(4)
    for col, label, value, sub in [
        (c1, "Total Amount Lent", f"${total_lent:,.0f}", "across all lenders"),
        (c2, "Avg Lender Rating", f"{avg_rating:.2f}", "out of 5"),
        (c3, "Completed Fundings", f"{total_completed:,}", "fully settled"),
        (c4, "Cancelled Fundings", f"{total_cancelled:,}", "withdrawn"),
    ]:
        col.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Top 20 Lenders by Amount Lent</div>', unsafe_allow_html=True)
        top20 = df.nlargest(20, "total_amount_lent")
        fig = go.Figure(go.Bar(
            x=top20["total_amount_lent"].astype(float),
            y=top20["lender_name"],
            orientation="h",
            marker=dict(
                color=top20["total_amount_lent"].astype(float),
                colorscale=[[0,"#FCC8D1"],[1,"#F76A8A"]],
                showscale=False
            )
        ))
        apply_base(fig)
        fig.update_layout(
            yaxis=dict(autorange="reversed"),
            xaxis_title="Total Amount Lent ($)",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Fund Status Breakdown</div>', unsafe_allow_html=True)
        fund_totals = {
            "Completed":  int(df["completed_fundings"].sum()),
            "Pending":    int(df["pending_fundings"].sum()),
            "Cancelled":  int(df["cancelled_fundings"].sum()),
            "Partial":    int(df["partial_fundings"].sum()),
        }
        fig = go.Figure(go.Pie(
            labels=list(fund_totals.keys()),
            values=list(fund_totals.values()),
            hole=0.55,
            marker_colors=["#6BCB77","#FFB347","#F76A8A","#7C6AF7"],
            textinfo="percent+label",
            textfont_size=13,
        ))
        apply_base(fig)
        fig.update_layout(showlegend=False, margin=dict(l=16,r=16,t=16,b=16))
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Rating vs Total Amount Lent</div>', unsafe_allow_html=True)
        fig = px.scatter(
            df.dropna(subset=["avg_rating"]),
            x="total_amount_lent",
            y="avg_rating",
            hover_name="lender_name",
            size="total_loans_funded",
            color="avg_interest_rate",
            color_continuous_scale=[[0,"#BAB0FB"],[1,"#7C6AF7"]],
            labels={
                "total_amount_lent": "Total Amount Lent ($)",
                "avg_rating": "Avg Rating",
                "avg_interest_rate": "Avg Interest Rate"
            }
        )
        apply_base(fig)
        fig.update_layout(yaxis_range=[0,5])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Lender Rating Distribution</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Histogram(
            x=df.dropna(subset=["avg_rating"])["avg_rating"].astype(float),
            nbinsx=10,
            marker_color="#F76A8A",
            opacity=0.85
        ))
        apply_base(fig)
        fig.update_layout(xaxis_title="Avg Rating", yaxis_title="Lender Count")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Full Lender Performance Table</div>', unsafe_allow_html=True)
    perf_df = df[[
        "lender_name","total_loans_funded","total_amount_lent",
        "avg_loan_amount","avg_interest_rate","completed_fundings",
        "cancelled_fundings","total_disputes","avg_rating"
    ]].copy()
    perf_df.columns = [
        "Lender","Loans Funded","Total Lent ($)","Avg Loan ($)",
        "Avg Rate (%)","Completed","Cancelled","Disputes","Avg Rating"
    ]
    st.dataframe(perf_df, use_container_width=True, hide_index=True)


# ── PAGE 4: REPAYMENT HEALTH ─────────────────────────────────────────────────
elif page == "Repayment Health":

    st.markdown("""
        <div class="page-header">
            <div class="accent-bar"></div>
            <div class="page-title">Repayment Health</div>
            <div class="page-subtitle">Outstanding balances, repayment progress, overdue loans and payment health across the portfolio</div>
        </div>
    """, unsafe_allow_html=True)

    df = run_query("SELECT * FROM vw_repayment_health")

    total_outstanding = float(df["outstanding_balance"].sum())
    total_paid        = float(df["total_paid"].sum())
    overdue_count     = int((df["payment_health"] == "Overdue").sum())
    fully_paid_count  = int((df["repayment_status"] == "Fully Paid").sum())

    c1, c2, c3, c4 = st.columns(4)
    for col, label, value, sub in [
        (c1, "Total Outstanding", f"${total_outstanding:,.0f}", "yet to be repaid"),
        (c2, "Total Repaid",      f"${total_paid:,.0f}",        "collected to date"),
        (c3, "Overdue Loans",     f"{overdue_count:,}",         "past due date"),
        (c4, "Fully Paid",        f"{fully_paid_count:,}",      "completed loans"),
    ]:
        col.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Repayment Status Breakdown</div>', unsafe_allow_html=True)
        status_counts = df["repayment_status"].value_counts().reset_index()
        status_counts.columns = ["Status","Count"]
        fig = go.Figure(go.Pie(
            labels=status_counts["Status"],
            values=status_counts["Count"],
            hole=0.55,
            marker_colors=["#6BCB77","#7C6AF7","#F76A8A"],
            textinfo="percent+label",
            textfont_size=13,
        ))
        apply_base(fig)
        fig.update_layout(showlegend=False, margin=dict(l=16,r=16,t=16,b=16))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Payment Health Breakdown</div>', unsafe_allow_html=True)
        health_counts = df["payment_health"].value_counts().reset_index()
        health_counts.columns = ["Health","Count"]
        color_map = {
            "Overdue":  "#F76A8A",
            "Due Soon": "#FFB347",
            "On Track": "#6BCB77"
        }
        fig = go.Figure(go.Bar(
            x=health_counts["Health"],
            y=health_counts["Count"],
            marker_color=[color_map.get(h, "#7C6AF7") for h in health_counts["Health"]],
        ))
        apply_base(fig)
        fig.update_layout(xaxis_title="", yaxis_title="Number of Loans", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Repayment Completion Distribution</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Histogram(
            x=df["repayment_pct"].astype(float),
            nbinsx=20,
            marker_color="#7C6AF7",
            opacity=0.85
        ))
        apply_base(fig)
        fig.update_layout(xaxis_title="Repayment Completion (%)", yaxis_title="Loan Count")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Outstanding Balance vs Loan Amount</div>', unsafe_allow_html=True)
        color_map_plotly = {
            "Overdue":  "#F76A8A",
            "Due Soon": "#FFB347",
            "On Track": "#6BCB77"
        }
        fig = px.scatter(
            df,
            x="loan_amount",
            y="outstanding_balance",
            color="payment_health",
            hover_name="borrower_name",
            color_discrete_map=color_map_plotly,
            labels={
                "loan_amount": "Original Loan Amount ($)",
                "outstanding_balance": "Outstanding Balance ($)",
                "payment_health": "Payment Health"
            }
        )
        apply_base(fig)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Repayment Health Table</div>', unsafe_allow_html=True)
    filter_opt = st.selectbox(
        "Filter by payment health",
        ["All","Overdue","Due Soon","On Track"]
    )
    filtered = df if filter_opt == "All" else df[df["payment_health"] == filter_opt]
    table_df = filtered[[
        "borrower_name","lender_name","loan_amount",
        "total_paid","outstanding_balance","repayment_pct",
        "repayment_status","payment_health"
    ]].copy()
    table_df.columns = [
        "Borrower","Lender","Loan Amount ($)","Total Paid ($)",
        "Outstanding ($)","Repaid (%)","Repayment Status","Payment Health"
    ]
    st.dataframe(table_df, use_container_width=True, hide_index=True)