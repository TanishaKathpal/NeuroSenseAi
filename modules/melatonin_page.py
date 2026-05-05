import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt


def show_melatonin():

    st.header("🌙 Melatonin Sleep Regulation Detection")

    model = joblib.load("models/melatonin_model.pkl")

    st.subheader("Enter Sleep & Lifestyle Data")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.number_input("Age", 10, 100, 25)
        sleep_duration = st.number_input("Sleep Duration (hours)", 0.0, 12.0, 7.0)
        sleep_quality = st.number_input("Quality of Sleep", 1, 10, 6)
        activity = st.number_input("Physical Activity Level", 0, 100, 40)

    with col2:
        stress = st.number_input("Stress Level", 0, 10, 5)
        bmi = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"])
        heart_rate = st.number_input("Heart Rate", 40, 150, 70)
        bp_sys = st.number_input("Systolic BP", 80, 200, 120)
        bp_dia = st.number_input("Diastolic BP", 50, 130, 80)

    if st.button("Predict Melatonin Regulation"):

        gender_val = 1 if gender == "Male" else 0

        bmi_map = {
            "Normal": 0,
            "Overweight": 1,
            "Obese": 2
        }

        data = pd.DataFrame({

            "Gender":[gender_val],
            "Age":[age],
            "Sleep Duration":[sleep_duration],
            "Quality of Sleep":[sleep_quality],
            "Physical Activity Level":[activity],
            "Stress Level":[stress],
            "BMI Category":[bmi_map[bmi]],
            "Heart Rate":[heart_rate],
            "BP_sys":[bp_sys],
            "BP_dia":[bp_dia]

        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 0:

            st.success("Normal Melatonin Regulation")

            st.write("""
**Interpretation**

• Healthy circadian rhythm  
• Balanced melatonin secretion during night  
• Good sleep duration and recovery  
• Stable physiological indicators
""")

        elif prediction == 1:

            st.warning("Possible Insomnia")

            st.write("""
**Interpretation**

• Reduced melatonin production at night  
• Difficulty initiating or maintaining sleep  
• Possible stress or lifestyle imbalance  
• Irregular sleep patterns
""")

        else:

            st.error("Possible Sleep Apnea")

            st.write("""
**Interpretation**

• Disrupted sleep cycles during the night  
• Possible breathing interruptions while sleeping  
• Poor oxygen regulation during sleep  
• Reduced deep sleep quality
""")

    st.divider()

    st.subheader("Sleep Analysis")

    col1, col2 = st.columns(2)

    # Feature Importance Graph
    with col1:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_

            features = [
                "Gender",
                "Age",
                "Sleep Duration",
                "Quality of Sleep",
                "Physical Activity Level",
                "Stress Level",
                "BMI Category",
                "Heart Rate",
                "BP_sys",
                "BP_dia"
            ]

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.barh(features, importance)
            ax.set_title("Sleep Feature Importance")

            st.pyplot(fig)

    # Sleep Pattern Graph
    with col2:

        if st.button("Show Sleep Pattern"):

            signal = np.random.normal(7, 0.5, 200)

            fig, ax = plt.subplots(figsize=(4,1.5))

            ax.plot(signal)

            ax.set_title("Simulated Sleep Duration")
            ax.set_xlabel("Days")
            ax.set_ylabel("Sleep Hours")

            st.pyplot(fig)