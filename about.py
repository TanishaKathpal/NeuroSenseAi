import streamlit as st


def show_about():

    if "platform_info" not in st.session_state:
        st.session_state.platform_info = None


    # ---------- CARD STYLE ----------

    st.markdown("""
    <style>

    .bio-card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    padding:22px;
    border-radius:16px;
    margin-bottom:18px;
    backdrop-filter: blur(10px);
    transition:all 0.3s ease;
    }

    .bio-card:hover{
    border:1px solid #38bdf8;
    box-shadow:0 0 25px rgba(56,189,248,0.6);
    transform:translateY(-6px);
    }

    .platform-card{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.08);
    padding:30px;
    border-radius:18px;
    height:230px;
    backdrop-filter: blur(10px);
    display:flex;
    flex-direction:column;
    justify-content:center;
    text-align:center;
    transition:all 0.3s ease;
    }

    .platform-card:hover{
    border:1px solid #6366f1;
    box-shadow:0 0 25px rgba(99,102,241,0.6);
    transform:translateY(-6px);
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------- HERO ----------

    st.markdown("""
    <div style="
    background: linear-gradient(135deg,#020617,#0f172a,#020617);
    padding:70px;
    border-radius:20px;
    text-align:center;
    margin-bottom:40px;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 15px rgba(99,102,241,0.45);
    ">

    <div style="font-size:70px;font-weight:900;
    background: linear-gradient(90deg,#22d3ee,#6366f1,#a855f7,#22d3ee);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;">
    🧠 NeuroSenseAI
    </div>

    <div style="font-size:24px;color:#cbd5f5;margin-top:15px;">
    Biosignal-Based Neurochemical Activity Prediction Platform
    </div>

    <div style="color:#94a3b8;margin-top:20px;font-size:18px;">
    AI-powered biomedical system that estimates neurochemical biomarkers
    using physiological biosignals and machine learning.
    </div>

    </div>
    """, unsafe_allow_html=True)


    st.write("""
NeuroSenseAI analyzes physiological biosignals such as **EEG, ECG, HRV and GSR**
to estimate neurotransmitter activity related to **stress, mood, cognition and sleep**.
""")


    st.markdown("---")


    # ---------- BIOMARKERS ----------

    st.header("Supported Neurochemical Modules")


    def biomarker_card(icon,title,text,button,page):

        st.markdown(f"""
        <div class="bio-card">
        <h4>{icon} {title}</h4>
        <p style="color:#94a3b8">{text}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(button):
            st.session_state.page = page


    col1,col2,col3 = st.columns(3)


    with col1:

        biomarker_card("🧠","Dopamine","Motivation & reward signaling",
        "Open Dopamine Module","Dopamine")

        biomarker_card("⚡","Norepinephrine","Stress & alertness response",
        "Open Norepinephrine Module","Norepinephrine")

        biomarker_card("😴","Melatonin","Sleep regulation",
        "Open Melatonin Module","Melatonin")


    with col2:

        biomarker_card("😊","Serotonin","Mood regulation",
        "Open Serotonin Module","Serotonin")

        biomarker_card("🎯","Acetylcholine","Cognitive processing",
        "Open Acetylcholine Module","Acetylcholine")

        biomarker_card("💊","Endorphin","Pain relief & emotional balance",
        "Open Endorphin Module","Endorphin")

        biomarker_card("🤝","Oxytocin","Social bonding & trust",
        "Open Oxytocin Module","Oxytocin")


    with col3:

        biomarker_card("🧘","GABA","Relaxation & neural inhibition",
        "Open GABA Module","GABA")

        biomarker_card("🔥","Glutamate","Learning & neural excitation",
        "Open Glutamate Module","Glutamate")

        biomarker_card("🚨","Adrenaline","Fight-or-flight response",
        "Open Adrenaline Module","Adrenaline")


    st.markdown("---")


    # ---------- PLATFORM OVERVIEW ----------

    st.header("Platform Overview")

    col1, col2, col3 = st.columns(3)


    def platform_card(title,text):

        st.markdown(f"""
        <div class="platform-card">
        <h3>{title}</h3>
        <p style="color:#94a3b8">{text}</p>
        </div>
        """, unsafe_allow_html=True)


    with col1:

        platform_card(
            "🤖 AI Models",
            "Multiple machine learning models trained to detect neurotransmitter biomarkers using biosignal data."
        )

        st.write("")
        st.write("")

        if st.button("View Details", key="models"):
            st.session_state.platform_info="models"


    with col2:

        platform_card(
            "📊 Biosignal Analysis",
            "Integration of EEG, ECG, HRV and GSR signals for multimodal physiological analysis."
        )

        st.write("")
        st.write("")

        if st.button("View Details", key="biosignal"):
            st.session_state.platform_info="biosignal"


    with col3:

        platform_card(
            "🧠 Neurochemical Insights",
            "AI-driven predictions related to stress, cognition, mood and sleep regulation."
        )

        st.write("")
        st.write("")

        if st.button("View Details", key="insights"):
            st.session_state.platform_info="insights"


    # ---------- INFO BOX ----------

    if st.session_state.platform_info == "models":

        st.info("""
AI Models

NeuroSenseAI uses Random Forest machine learning models
trained on biosignal datasets to estimate neurotransmitter activity.
""")


    elif st.session_state.platform_info == "biosignal":

        st.info("""
Biosignal Analysis

• EEG  
• ECG  
• HRV  
• GSR
""")


    elif st.session_state.platform_info == "insights":

        st.info("""
Neurochemical Insights

• Dopamine  
• Serotonin  
• GABA  
• Glutamate  
• Oxytocin  
• Melatonin
""")


    st.markdown("---")

    st.success("NeuroSenseAI — AI-driven biosignal biomarker detection platform.")