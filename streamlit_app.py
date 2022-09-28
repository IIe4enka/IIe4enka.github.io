import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

dataset_url = "projectdata.csv"

def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

st.markdown("### First chart")
fig2 = px.histogram(data_frame=df, x="Учебный")
st.write(fig2)

st.markdown("### Detailed Data View")
st.dataframe(df)
