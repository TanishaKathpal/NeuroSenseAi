import streamlit as st

from modules.dopamine_page import show_dopamine
from modules.serotonin_page import show_serotonin
from modules.norepinephrine_page import show_norepinephrine
from modules.acetylcholine_page import show_acetylcholine
from modules.gaba_page import show_gaba
from modules.glutamate_page import show_glutamate
from modules.melatonin_page import show_melatonin
from modules.endorphin_page import show_endorphin
from modules.oxytocin_page import show_oxytocin
from modules.adrenaline_page import show_adrenaline
from about import show_about

st.set_page_config(page_title="NeuroSenseAI", layout="wide")

# -------------------------------------------------
# GLOBAL STYLE
# -------------------------------------------------

st.markdown("""
<style>

html{
scroll-behavior:smooth;
}

[data-testid="stAppViewContainer"]{
background: radial-gradient(circle at top,#0f172a,#020617);
color:white;
font-family: "Segoe UI", sans-serif;
}

/* ---------------- SPACE ABOVE CONTENT ---------------- */

.block-container{
padding-top:20px;
}

/* ---------------- SIDEBAR ---------------- */

section[data-testid="stSidebar"]{
margin-top:0px;
background:linear-gradient(180deg,#020617,#0f172a);
border-right:1px solid rgba(255,255,255,0.05);
width:260px;
padding-top:0px;
}

section[data-testid="stSidebar"] h2{
font-size:22px;
font-weight:700;
margin-bottom:15px;
color:#e2e8f0;
}

section[data-testid="stSidebar"] label{
background:rgba(255,255,255,0.03);
border:1px solid rgba(255,255,255,0.06);
padding:10px 12px;
border-radius:10px;
font-size:15px;
color:#cbd5f5;
margin-bottom:8px;
transition:all 0.25s ease;
}

section[data-testid="stSidebar"] label:hover{
background:rgba(59,130,246,0.15);
border:1px solid #3b82f6;
color:white;
transform:translateX(5px);
box-shadow:0 0 12px rgba(59,130,246,0.4);
}

/* ---------------- TEXT ---------------- */

p,li,span{
color:#e5e7eb !important;
}

h1,h2,h3,h4{
color:white !important;
}

/* ---------------- INPUT FIX ---------------- */

[data-testid="stNumberInput"] input{
background:#111827 !important;
color:white !important;
border:1px solid rgba(255,255,255,0.15) !important;
}

[data-testid="stTextInput"] input{
background:#111827 !important;
color:white !important;
}

[data-testid="stSelectbox"] div{
background:#111827 !important;
color:white !important;
}

/* Dropdown options */

div[role="option"]{
background:#111827 !important;
color:white !important;
}

div[role="option"]:hover{
background:#1f2937 !important;
}

/* Buttons */

.stButton button{
background:linear-gradient(90deg,#6366f1,#8b5cf6) !important;
color:white !important;
border:none !important;
border-radius:8px !important;
padding:8px 16px !important;
}

.stButton button:hover{
box-shadow:0 0 10px rgba(99,102,241,0.6);
}

label{
color:#cbd5f5 !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page="About"


# -------------------------------------------------
# SIDEBAR LOGO (TOP LEFT)
# -------------------------------------------------

st.sidebar.markdown("""
<div style="
display:flex;
align-items:center;
gap:10px;
margin-bottom:12px;
white-space:nowrap;
">

<span style="
font-size:26px;
background:linear-gradient(90deg,#22d3ee,#6366f1,#a855f7);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
font-weight:900;
">
🧠
</span>

<span style="
font-size:22px;
font-weight:900;
background:linear-gradient(90deg,#22d3ee,#6366f1,#a855f7);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
">
NeuroSenseAI
</span>

</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------

pages=[
"About",
"Dopamine",
"Serotonin",
"Norepinephrine",
"Acetylcholine",
"GABA",
"Glutamate",
"Melatonin",
"Endorphin",
"Oxytocin",
"Adrenaline"
]

st.sidebar.title("Modules")

selected_page=st.sidebar.radio(
"Navigate",
pages,
index=pages.index(st.session_state.page)
)

if selected_page!=st.session_state.page:
    st.session_state.page=selected_page

page=st.session_state.page


# -------------------------------------------------
# ROUTING
# -------------------------------------------------

if page=="About":
    show_about()

elif page=="Dopamine":
    show_dopamine()

elif page=="Serotonin":
    show_serotonin()

elif page=="Norepinephrine":
    show_norepinephrine()

elif page=="Acetylcholine":
    show_acetylcholine()

elif page=="GABA":
    show_gaba()

elif page=="Glutamate":
    show_glutamate()

elif page=="Melatonin":
    show_melatonin()

elif page=="Endorphin":
    show_endorphin()

elif page=="Oxytocin":
    show_oxytocin()

elif page=="Adrenaline":
    show_adrenaline()