import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("StatBot Pro")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.write(df)

    st.subheader("Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        selected_col = st.selectbox(
            "Choose column for graph",
            numeric_cols
        )

        fig, ax = plt.subplots()
        df[selected_col].plot(ax=ax)

        st.pyplot(fig)