import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_norepinephrine():

    st.header("Norepinephrine Stress Detection")

    model = joblib.load("models/norepinephrine_model.pkl")

    st.subheader("Enter HRV Physiological Features")

    col1, col2 = st.columns(2)

    with col1:
        hr = st.number_input("Heart Rate (HR)", 40.0, 150.0, 75.0)
        rmssd = st.number_input("RMSSD", 1.0, 50.0, 15.0)
        sdrr = st.number_input("SDRR", 1.0, 150.0, 40.0)

    with col2:
        lf = st.number_input("LF Power", 0.0, 5000.0, 300.0)
        hf = st.number_input("HF Power", 0.0, 5000.0, 200.0)
        lf_hf = st.number_input("LF/HF Ratio", 0.0, 50.0, 1.5)

    if st.button("Predict Stress Condition"):

        data = pd.DataFrame({
            "HR":[hr],
            "RMSSD":[rmssd],
            "SDRR":[sdrr],
            "LF":[lf],
            "HF":[hf],
            "LF_HF":[lf_hf]
        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 0:

            st.success("No Stress Condition")

            st.write("""
Interpretation:

• Balanced autonomic nervous system  
• Normal norepinephrine activity  
• Stable physiological state
""")

        elif prediction == 1:

            st.warning("Interruption Stress")

            st.write("""
Interpretation:

• Increased cognitive load  
• Elevated norepinephrine release  
• Possible attention disruption
""")

        elif prediction == 2:

            st.error("Time Pressure Stress")

            st.write("""
Interpretation:

• High sympathetic nervous system activity  
• Elevated norepinephrine levels  
• Strong stress response
""")

    st.divider()

    st.subheader("Optional Physiological Analysis")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Show HRV Feature Importance"):

            importance = model.feature_importances_

            features = [
                "HR",
                "RMSSD",
                "SDRR",
                "LF",
                "HF",
                "LF_HF"
            ]

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.barh(features, importance)
            ax.set_title("HRV Feature Importance")

            st.pyplot(fig)

    with col2:

        if st.button("Show Heart Rate Simulation"):

            signal = np.random.normal(75,5,200)

            fig, ax = plt.subplots(figsize=(4,1.5))

            ax.plot(signal)

            ax.set_title("Simulated Heart Rate Signal")
            ax.set_xlabel("Time")
            ax.set_ylabel("HR")

            st.pyplot(fig)