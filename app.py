import streamlit as st
import plotly.graph_objects as go

from pdf_reader import extract_text
from text_cleaner import clean_text
from clause_splitter import split_clauses
from risk_engine import detect_risk
from ai_engine import explain_clause_ai
from contract_analyzer import detect_contract_redflags


# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="ClauseGuard AI",
    layout="wide"
)


# =====================================
# SIDEBAR PANEL (LIKE IMAGE)
# =====================================
with st.sidebar:

    st.markdown("## 🧠 ClauseGuard AI")

    st.markdown("---")

    st.markdown("### Dashboard")

    st.markdown("""
✅ Contract Analyzer  
📄 Clause Intelligence  
🚨 Risk Detection  
📊 Risk Score Engine  
🔒 Privacy Safe  
""")

    st.markdown("---")

    st.markdown(
    """
    **AI Contract Safety Tool**

    Analyze agreements before signing.
    """
    )



# =====================================
# UI STYLE
# =====================================
st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#eef2ff,
#f8fafc
);
}

/* Main container */
.block-container{
background:rgba(255,255,255,0.85);
padding:2.5rem;
border-radius:20px;
box-shadow:0px 15px 40px rgba(0,0,0,0.08);
}

/* HERO */
.hero{
text-align:center;
padding-bottom:25px;
}

.hero h1{
font-size:48px;
font-weight:800;
color:#1e293b;
}

.highlight{
color:#4FD1C5;
}

.hero p{
font-size:18px;
color:#475569;
max-width:800px;
margin:auto;
}

/* Feature Cards */
.feature-card{
background:white;
padding:22px;
border-radius:16px;
box-shadow:0px 8px 20px rgba(0,0,0,0.06);
margin-bottom:18px;
transition:.3s;
}

.feature-card:hover{
transform:translateY(-5px);
}

/* Clause box */
.clause-card{
background:white;
padding:18px;
border-radius:14px;
margin-top:12px;
box-shadow:0px 6px 18px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)



# =====================================
# HERO
# =====================================
st.markdown("""
<div class="hero">

<h1>
Decode Your Agreement with
<span class="highlight">Ease</span>
</h1>

<p>
ClauseGuard AI analyzes contracts and highlights hidden risks
so you understand agreements before accepting them.
</p>

</div>
""", unsafe_allow_html=True)



# =====================================
# INPUT
# =====================================
st.header("Choose Input Method")

input_mode = st.radio(
    "Select Input",
    ["Upload PDF", "Paste Contract Text"]
)

file=None
manual_text=None

if input_mode=="Upload PDF":

    file=st.file_uploader(
        "Upload Contract",
        type=["pdf"]
    )

else:

    manual_text=st.text_area(
        "Paste Agreement / Contract",
        height=260
    )


analyze = st.button(
    "🔍 Analyze Contract",
    use_container_width=True
)



# =====================================
# GAUGE
# =====================================
def risk_gauge(score):

    fig=go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text':"Overall Contract Risk"},

        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':"#1e293b"},
            'steps':[
                {'range':[0,40],'color':"#22c55e"},
                {'range':[40,70],'color':"#facc15"},
                {'range':[70,100],'color':"#ef4444"},
            ],
        }
    ))

    fig.update_layout(height=320)

    return fig



# =====================================
# CACHE AI
# =====================================
@st.cache_data(show_spinner=False)
def cached_ai_analysis(clause,risk):

    result = explain_clause_ai(clause,risk)

    if isinstance(result,str):
        return {"impact":result}

    if result is None:
        return {"impact":"AI unavailable"}

    return result



# =====================================
# ANALYSIS
# =====================================
if analyze:

    process_text=None

    if file:
        process_text=extract_text(file)

    elif manual_text and manual_text.strip():
        process_text=manual_text

    if not process_text:
        st.warning("Please upload or paste contract first.")
        st.stop()


    with st.spinner("🧠 AI analyzing agreement..."):

        clean=clean_text(process_text)
        clauses=split_clauses(clean)


    st.success("✅ Contract Analyzed Successfully")


    # =====================
    # RED FLAGS
    # =====================
    redflags=detect_contract_redflags(clauses)

    if redflags:

        st.subheader("🚨 Contract Red Flags")

        for r in redflags:
            st.warning(r)



    # =====================
    # CLAUSE BREAKDOWN
    # =====================
    st.header("📌 Clause Breakdown")

    total_score=0
    clause_count=0


    for name,clause in clauses.items():

        risk,score=detect_risk(clause)

        total_score+=score
        clause_count+=1

        st.markdown(
        f'<div class="clause-card"><h3>{name.upper()}</h3></div>',
        unsafe_allow_html=True
        )

        if risk=="High":
            st.error(f"🚨 Risk Level: {risk}")

        elif risk=="Medium":
            st.warning(f"⚠ Risk Level: {risk}")

        else:
            st.success(f"✅ Risk Level: {risk}")


        analysis=cached_ai_analysis(clause,risk)

        with st.expander("🔎 Clause Intelligence"):

            impact=analysis.get("impact","")

            if impact:
                st.write(impact)



    # =====================
    # FINAL SCORE
    # =====================
    if clause_count>0:

        final_score=int(total_score/clause_count)

        st.divider()
        st.header("📊 Overall Contract Risk")

        st.plotly_chart(
            risk_gauge(final_score),
            use_container_width=True
        )

        if final_score>=70:
            st.error("🚨 HIGH RISK CONTRACT")

        elif final_score>=40:
            st.warning("⚠ MEDIUM RISK CONTRACT")

        else:
            st.success("✅ LOW RISK CONTRACT")



    # =====================================
    # FEATURES AFTER ANALYSIS
    # =====================================
    st.divider()

    st.markdown("## What Makes CLAUSEGUARD AI Different?")

    c1,c2=st.columns(2)
    c3,c4=st.columns(2)

    with c1:
        st.markdown("""
        <div class="feature-card">
        <h4>⚙️ Advanced AI Technology</h4>
        Cutting-edge algorithms analyze agreements clearly.
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
        <h4>👁️ User-Friendly Design</h4>
        Insights delivered without legal jargon.
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
        <h4>💰 Time and Money Savings</h4>
        Detect risks early and avoid surprises.
        </div>
        """,unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="feature-card">
        <h4>🛡️ Privacy First</h4>
        Your uploaded contracts remain confidential.
        </div>

        """,unsafe_allow_html=True)
