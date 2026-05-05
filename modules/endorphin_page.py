import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt


def show_endorphin():

    st.header("Endorphin Psychological Biomarker Detection")

    model = joblib.load("models/endorphin_model.pkl")

    st.subheader("Enter Physiological Signals")

    col1, col2 = st.columns(2)

    with col1:

        hrv = st.number_input("HRV (ms)",20.0,200.0,50.0)
        gsr = st.number_input("GSR (µS)",0.0,10.0,1.0)

        eeg1 = st.number_input("EEG Alpha Band",0.0,10.0,1.0)
        eeg2 = st.number_input("EEG Beta Band",0.0,10.0,1.0)
        eeg3 = st.number_input("EEG Gamma Band",0.0,10.0,1.0)

        heart_rate = st.number_input("Heart Rate (BPM)",40.0,150.0,75.0)

    with col2:

        bp_sys = st.number_input("Systolic BP",80,200,120)
        bp_dia = st.number_input("Diastolic BP",50,130,80)

        respiration = st.number_input("Respiration Rate",5.0,40.0,16.0)

        oxygen = st.number_input("Oxygen Saturation (%)",80.0,100.0,97.0)

        skin_temp = st.number_input("Skin Temp (°C)",30.0,40.0,36.5)

    # Auto-generated contextual features
    cognitive_load = np.random.randint(0,3)
    mood_state = np.random.randint(0,4)
    task_type = np.random.randint(0,3)
    gender = np.random.randint(0,2)
    education = np.random.randint(0,4)
    major = np.random.randint(0,4)
    focus = np.random.uniform(60,200)
    noise = np.random.uniform(20,60)
    age = np.random.randint(18,40)

    if st.button("Predict Endorphin Activity"):

        data = pd.DataFrame({

            "HRV (ms)":[hrv],
            "GSR (µS)":[gsr],

            "EEG_band1":[eeg1],
            "EEG_band2":[eeg2],
            "EEG_band3":[eeg3],

            "BP_sys":[bp_sys],
            "BP_dia":[bp_dia],

            "Oxygen Saturation (%)":[oxygen],
            "Heart Rate (BPM)":[heart_rate],
            "Ambient Noise (dB)":[noise],

            "Cognitive Load":[cognitive_load],
            "Mood State":[mood_state],

            "Respiration Rate (BPM)":[respiration],
            "Skin Temp (°C)":[skin_temp],
            "Focus Duration (s)":[focus],

            "Task Type":[task_type],
            "Age":[age],
            "Gender":[gender],
            "Educational Level":[education],
            "Study Major":[major]

        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("High Endorphin Activity")

            st.write("""
• Positive psychological state  
• Relaxation or emotional balance  
• Natural pain-relief response
""")

        else:

            st.warning("Low Endorphin Activity")

            st.write("""
• Stress or anxiety detected  
• Reduced natural mood regulation  
• Possible emotional tension
""")
            
    st.divider()

    st.subheader("Physiological Analysis")

    col1, col2 = st.columns(2)

    # Heart Rate Signal
    with col1:

        if st.button("Show Heart Rate Pattern"):

            signal = np.random.normal(75,5,200)

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.plot(signal)

            ax.set_title("Simulated Heart Rate Pattern")
            ax.set_xlabel("Time")
            ax.set_ylabel("BPM")

            st.pyplot(fig)

    # Endorphin Activity Simulation
    with col2:

        if st.button("Show Endorphin Activity Pattern"):

            x = np.linspace(0,10,100)
            y = np.sin(x) + np.random.normal(0,0.2,100)

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.plot(x,y)

            ax.set_title("Simulated Endorphin Activity")
            ax.set_xlabel("Time")
            ax.set_ylabel("Activity Level")

            st.pyplot(fig)