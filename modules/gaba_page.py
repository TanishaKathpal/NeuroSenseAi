import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_gaba():

    st.header("GABA Neural Activity Detection")

    model = joblib.load("models/gaba_model.pkl")

    st.subheader("Enter EEG Brainwave Features")

    col1, col2 = st.columns(2)

    with col1:
        delta = st.number_input("Delta Waves", 0.0, 100000.0, 20000.0)
        theta = st.number_input("Theta Waves", 0.0, 100000.0, 18000.0)
        low_alpha = st.number_input("Low Alpha Waves", 0.0, 100000.0, 15000.0)

    with col2:
        high_alpha = st.number_input("High Alpha Waves", 0.0, 100000.0, 14000.0)
        low_beta = st.number_input("Low Beta Waves", 0.0, 100000.0, 12000.0)
        high_beta = st.number_input("High Beta Waves", 0.0, 100000.0, 11000.0)

    if st.button("Predict GABA Activity"):

        data = pd.DataFrame({
            "delta": [delta],
            "theta": [theta],
            "lowAlpha": [low_alpha],
            "highAlpha": [high_alpha],
            "lowBeta": [low_beta],
            "highBeta": [high_beta]
        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("High GABA Activity")

            st.write("""
Interpretation:

• Increased inhibitory neurotransmission  
• Higher relaxation or meditation state  
• Reduced neural overactivity
""")

        else:

            st.warning("Low GABA Activity")

            st.write("""
Interpretation:

• Lower inhibitory signaling  
• Possible neural excitation or stress  
• Reduced relaxation response
""")

    st.divider()

    st.subheader("EEG Visualization")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Show EEG Brainwave Signal"):

            signal = np.random.normal(0,1,200)

            fig, ax = plt.subplots(figsize=(4,2.5))
            ax.plot(signal)

            ax.set_title("Simulated EEG Signal")
            ax.set_xlabel("Time")
            ax.set_ylabel("Amplitude")

            st.pyplot(fig)

    with col2:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_

            features = [
                "delta",
                "theta",
                "lowAlpha",
                "highAlpha",
                "lowBeta",
                "highBeta"
            ]

            fig, ax = plt.subplots(figsize=(4,2.5))
            ax.barh(features, importance)

            ax.set_title("EEG Feature Importance for GABA")

            st.pyplot(fig)