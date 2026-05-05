import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_serotonin():

    st.header("Serotonin Behavioral Response Detection")

    model = joblib.load("models/Seratonin_model.pkl")

    st.subheader("Enter Behavioral Signals")

    col1, col2 = st.columns(2)

    with col1:
        odor = st.number_input("Odor Type", 1, 5, 1)
        total_licks = st.number_input("Total Licks", 0, 50, 10)

    with col2:
        first_lick_time = st.number_input("First Lick Time", 0, 10000, 2000)
        lick_rate = st.number_input("Lick Rate", 0.0, 1.0, 0.01)

    if st.button("Predict Serotonin Response"):

        data = pd.DataFrame({
            "odor":[odor],
            "total_licks":[total_licks],
            "first_lick_time":[first_lick_time],
            "lick_rate":[lick_rate]
        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == 1:

            st.success("Positive Serotonin Reward Response")

            st.write("""
Possible interpretation:

• Strong reward signaling  
• Positive behavioral response  
• Increased motivation and engagement
""")

        else:

            st.warning("Neutral Serotonin Response")

            st.write("""
Possible interpretation:

• Weak reward activation  
• Neutral behavioral outcome  
• Reduced serotonin stimulation
""")

    st.divider()

    st.subheader("Behavioral Analysis")

    col1, col2 = st.columns(2)

    # Lick Signal Visualization
    with col1:

        if st.button("Show Licking Behavior Signal"):

            signal = np.zeros(1200)
            lick_events = np.random.randint(200,1000,12)

            signal[lick_events] = 1

            fig, ax = plt.subplots(figsize=(4,2.5))
            ax.plot(signal)

            ax.set_title("Licking Behavior Signal")
            ax.set_xlabel("Time Points")
            ax.set_ylabel("Lick Event")

            st.pyplot(fig)

    # Distribution of licking responses
    with col2:

        if st.button("Show Licking Distribution"):

            values = np.random.randint(0,25,150)

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.hist(values,bins=20)

            ax.set_title("Distribution of Licking Responses")
            ax.set_xlabel("Total Licks")

            st.pyplot(fig)