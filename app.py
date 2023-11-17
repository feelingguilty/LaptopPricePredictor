import pickle
import numpy as np 
import streamlit as st

df = pickle.load(open('df.pkl','rb'))
pipe = pickle.load(open('pipe.pkl','rb'))

st.title("Laptop Price Predictor")

company = st.selectbox('Brand',df['Company'].unique())
