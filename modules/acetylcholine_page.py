import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_acetylcholine():

    st.header("Acetylcholine Cognitive State Detection")

    model = joblib.load("models/AcetylCholine_model.pkl")

    st.subheader("Enter Physiological & Cognitive Signals")

    col1, col2 = st.columns(2)

    with col1:
        hrv = st.number_input("HRV (ms)", 10.0, 200.0, 50.0)
        gsr = st.number_input("GSR (µS)", 0.0, 1000.0, 300.0)
        heart_rate = st.number_input("Heart Rate (BPM)", 40.0, 180.0, 75.0)
        oxygen = st.number_input("Oxygen Saturation (%)", 80.0, 100.0, 97.0)
        respiration = st.number_input("Respiration Rate (BPM)", 5.0, 40.0, 16.0)
        skin_temp = st.number_input("Skin Temp (°C)", 30.0, 40.0, 36.5)

    with col2:
        cognitive_load = st.number_input("Cognitive Load", 0, 3, 1)
        mood_state = st.number_input("Mood State", 0, 3, 1)
        focus_duration = st.number_input("Focus Duration (s)", 0.0, 600.0, 120.0)
        task_type = st.number_input("Task Type", 0, 3, 1)
        eeg1 = st.number_input("EEG_band1", 0.0, 10.0, 1.0)
        eeg2 = st.number_input("EEG_band2", 0.0, 10.0, 1.0)
        eeg3 = st.number_input("EEG_band3", 0.0, 10.0, 1.0)

    if st.button("Predict Cognitive State"):

        data = pd.DataFrame({
            "HRV (ms)": [hrv],
            "GSR (μS)": [gsr],
            "Heart Rate (BPM)": [heart_rate],
            "Oxygen Saturation (%)": [oxygen],
            "Respiration Rate (BPM)": [respiration],
            "Skin Temp (°C)": [skin_temp],
            "Cognitive Load": [cognitive_load],
            "Mood State": [mood_state],
            "Focus Duration (s)": [focus_duration],
            "Task Type": [task_type],
            "EEG_band1": [eeg1],
            "EEG_band2": [eeg2],
            "EEG_band3": [eeg3]
        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("High Cognitive Stress State")

            st.write("""
Interpretation:

• Increased acetylcholine signaling  
• High cognitive load  
• Strong mental engagement or stress
""")

        else:

            st.info("Normal Cognitive State")

            st.write("""
Interpretation:

• Balanced neural activity  
• Moderate cognitive load  
• Stable physiological signals
""")

    st.divider()

    st.subheader("Signal Visualization")

    col1, col2 = st.columns(2)

    # Feature Importance Graph
    with col1:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_
            features = model.feature_names_in_

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.barh(features, importance)
            ax.set_title("Feature Importance")

            st.pyplot(fig)

    # Physiological Signal Graph
    with col2:

        if st.button("Show Physiological Signal Example"):

            signal = np.random.normal(75, 5, 200)

            fig, ax = plt.subplots(figsize=(4,1.5))

            ax.plot(signal)

            ax.set_title("Simulated Physiological Signal")
            ax.set_xlabel("Time")
            ax.set_ylabel("Signal")

            st.pyplot(fig)