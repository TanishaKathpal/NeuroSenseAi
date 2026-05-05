import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np


def show_dopamine():

    st.header("Dopamine Biomarker Detection")

    model = joblib.load("models/dopamine_model.pkl")

    st.subheader("Enter Biosensor Measurements")

    col1, col2 = st.columns(2)

    with col1:
        baseline_um = st.number_input("baseline uM", 0.0, 5.0, 0.5)
        baseline_dap = st.number_input("baseline DA/p", 0.0, 2000.0, 100.0)

    with col2:
        vmax = st.number_input("Baseline Vmax (nM/s)", 0.0, 10000.0, 2000.0)
        stim = st.number_input("stimulation (mA)", 0.0, 10.0, 2.0)

    if st.button("Predict Dopamine Level"):

        data = pd.DataFrame({
            "baseline uM":[baseline_um],
            "baseline DA/p":[baseline_dap],
            "Baseline Vmax (nM/s)":[vmax],
            "stimulation (mA)":[stim]
        })

        prediction = model.predict(data)[0]

        st.subheader("Prediction Result")

        if prediction == "Low":

            st.warning("Low Dopamine Activity")

            st.write("""
Possible interpretation:

• Reduced motivation  
• Fatigue or low reward response  
• Possible stress or depressive state  
• Reduced neural stimulation
""")

        elif prediction == "Medium":

            st.info("Moderate Dopamine Activity")

            st.write("""
Possible interpretation:

• Balanced reward signaling  
• Normal cognitive function  
• Stable motivation and attention
""")

        elif prediction == "High":

            st.success("High Dopamine Activity")

            st.write("""
Possible interpretation:

• Strong reward system activation  
• Increased motivation or stimulation  
• Possible excitement or cognitive engagement
""")

    st.divider()

    st.subheader("Analysis Visualizations")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Show Feature Importance"):

            importance = model.feature_importances_
            features = model.feature_names_in_

            fig, ax = plt.subplots(figsize=(4,2.5))
            ax.barh(features, importance)
            ax.set_title("Feature Importance")

            st.pyplot(fig)

    with col2:

        if st.button("Show Dopamine Response Graph"):

            x = np.linspace(0,10,50)
            y = x*0.3 + np.random.normal(0,0.2,50)

            fig, ax = plt.subplots(figsize=(4,2.5))

            ax.scatter(x,y)
            ax.set_xlabel("Stimulation (mA)")
            ax.set_ylabel("Dopamine Output (uM)")
            ax.set_title("Biosensor Dopamine Response")

            st.pyplot(fig)