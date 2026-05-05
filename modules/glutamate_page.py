import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_glutamate():

    st.header("Glutamate Neural Activity Detection")

    model = joblib.load("models/glutamate_model.pkl")

    st.subheader("Enter EEG Beta/Gamma Brainwave Features")

    col1, col2 = st.columns(2)

    with col1:
        low_beta = st.number_input("Low Beta Waves", 0.0, 100000.0, 20000.0)
        high_beta = st.number_input("High Beta Waves", 0.0, 100000.0, 22000.0)

    with col2:
        low_gamma = st.number_input("Low Gamma Waves", 0.0, 100000.0, 18000.0)
        high_gamma = st.number_input("High Gamma Waves", 0.0, 100000.0, 16000.0)

    if st.button("Predict Glutamate Activity"):

        data = pd.DataFrame({
            "lowBeta": [low_beta],
            "highBeta": [high_beta],
            "lowGamma": [low_gamma],
            "highGamma": [high_gamma]
        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("High Glutamate Activity")

            st.write("""
Interpretation:

• Increased excitatory neurotransmission  
• High cognitive stimulation  
• Strong neural activation
""")

        else:

            st.info("Normal Glutamate Activity")

            st.write("""
Interpretation:

• Balanced excitatory signaling  
• Stable neural communication  
• Moderate brain activity
""")

    st.divider()

    st.subheader("Optional EEG Visualization")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Show Gamma Wave Signal"):

            signal = np.random.normal(0,1,200)

            fig, ax = plt.subplots(figsize=(4,2.5))
            ax.plot(signal)

            ax.set_title("Simulated Gamma Wave Activity")
            ax.set_xlabel("Time")
            ax.set_ylabel("Amplitude")

            st.pyplot(fig)

    with col2:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_

            features = [
                "lowBeta",
                "highBeta",
                "lowGamma",
                "highGamma"
            ]

            fig, ax = plt.subplots(figsize=(4,2.5))
            ax.barh(features, importance)

            ax.set_title("EEG Feature Importance for Glutamate")

            st.pyplot(fig)