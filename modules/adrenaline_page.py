import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_adrenaline():

    st.header("Adrenaline Stress Biomarker Detection")

    model = joblib.load("models/adrenaline_model.pkl")

    st.subheader("Enter HRV Features")

    col1, col2 = st.columns(2)

    with col1:
        hr = st.number_input("Heart Rate (HR)", 40.0,150.0,75.0)
        rmssd = st.number_input("RMSSD",0.0,200.0,40.0)
        sdrr = st.number_input("SDRR",0.0,200.0,40.0)
        lf = st.number_input("LF Power",0.0,5000.0,500.0)

    with col2:
        hf = st.number_input("HF Power",0.0,5000.0,500.0)
        lf_hf = st.number_input("LF/HF Ratio",0.0,10.0,1.5)
        sd1 = st.number_input("SD1",0.0,100.0,20.0)
        sd2 = st.number_input("SD2",0.0,100.0,40.0)

    if st.button("Predict Adrenaline Level"):

        data = pd.DataFrame({

            "HR":[hr],
            "RMSSD":[rmssd],
            "SDRR":[sdrr],
            "LF":[lf],
            "HF":[hf],
            "LF_HF":[lf_hf],
            "SD1":[sd1],
            "SD2":[sd2]

        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 0:

            st.success("Low Adrenaline")

            st.write("""
Interpretation:

• Relaxed physiological state  
• Low stress response  
• Stable autonomic nervous system
""")

        elif prediction == 1:

            st.warning("Moderate Adrenaline")

            st.write("""
Interpretation:

• Mild stress response  
• Cognitive workload present  
• Increased alertness
""")

        else:

            st.error("High Adrenaline")

            st.write("""
Interpretation:

• High stress or pressure  
• Strong sympathetic nervous activation  
• Possible fight-or-flight response
""")

    st.divider()

    st.subheader("HRV Analysis")

    col1, col2 = st.columns(2)

    # Feature Importance
    with col1:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_

            features = [
                "HR",
                "RMSSD",
                "SDRR",
                "LF",
                "HF",
                "LF_HF",
                "SD1",
                "SD2"
            ]

            fig, ax = plt.subplots(figsize=(3.5,2.2))

            ax.barh(features, importance)
            ax.set_title("HRV Feature Importance")

            st.pyplot(fig)

    # HRV Signal Simulation
    with col2:

        if st.button("Show HRV Signal Example"):

            signal = np.random.normal(70,5,200)

            fig, ax = plt.subplots(figsize=(3.5,1.8))

            ax.plot(signal)

            ax.set_title("Simulated Heart Rate Variation")
            ax.set_xlabel("Time")
            ax.set_ylabel("HR")

            st.pyplot(fig)