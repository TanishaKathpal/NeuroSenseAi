import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_oxytocin():

    st.header("Oxytocin Social Bonding Biomarker")

    model = joblib.load("models/oxytocin_model.pkl")

    st.subheader("Enter ECG + GSR Features")

    col1, col2 = st.columns(2)

    with col1:
        ecg_mean = st.number_input("ECG Mean", -30.0, 30.0, -10.0)
        ecg_std = st.number_input("ECG Std", 0.0, 5.0, 0.5)

    with col2:
        gsr_mean = st.number_input("GSR Mean", 0.0, 2000.0, 300.0)
        gsr_std = st.number_input("GSR Std", 0.0, 200.0, 40.0)
        gsr_max = st.number_input("GSR Max", 0.0, 2000.0, 400.0)

    if st.button("Predict Oxytocin Level"):

        data = pd.DataFrame({

            "ecg_mean":[ecg_mean],
            "ecg_std":[ecg_std],
            "gsr_mean":[gsr_mean],
            "gsr_std":[gsr_std],
            "gsr_max":[gsr_max]

        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 0:

            st.warning("Low Oxytocin")

            st.write("""
Interpretation:

• Low emotional bonding signals  
• Reduced trust/social connection  
• Possible stress or discomfort
""")

        elif prediction == 1:

            st.info("Moderate Oxytocin")

            st.write("""
Interpretation:

• Neutral emotional state  
• Moderate social engagement  
• Stable physiological response
""")

        else:

            st.success("High Oxytocin")

            st.write("""
Interpretation:

• Strong social bonding signals  
• Emotional trust and connection  
• Positive emotional engagement
""")

    st.divider()

    st.subheader("Optional Signal Analysis")

    col1, col2 = st.columns(2)

    # Feature Importance
    with col1:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_

            features = [
                "ECG Mean",
                "ECG Std",
                "GSR Mean",
                "GSR Std",
                "GSR Max"
            ]

            fig, ax = plt.subplots(figsize=(3.5,2.2))

            ax.barh(features, importance)
            ax.set_title("Oxytocin Feature Importance")

            st.pyplot(fig)

    # ECG vs GSR Graph
    with col2:

        if st.button("Show ECG vs GSR Relationship"):

            ecg = np.random.normal(-10,3,100)
            gsr = np.random.normal(300,100,100)

            fig, ax = plt.subplots(figsize=(3.5,1.8))

            ax.scatter(ecg, gsr)

            ax.set_xlabel("ECG Mean")
            ax.set_ylabel("GSR Mean")
            ax.set_title("ECG vs GSR Relationship")

            st.pyplot(fig)