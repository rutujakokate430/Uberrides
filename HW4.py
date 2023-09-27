import plotly.express as px
import pandas as pd
import streamlit as st
st.title("Uber Rides in NYC")
df= pd.read_csv("Uber-Jan-Feb-FOIL.csv")
fig=px.bar(df, x="dispatching_base_number", y="trips")
st.plotly_chart(fig)
st.write("Table data for Uber rides in NYC")
st.write(df)
