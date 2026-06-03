import streamlit as st
import pandas as pd
import numpy as np

# පිටුව ලස්සන කරන්න Setup එක
st.set_page_config(page_title="AI Smart Predictor", page_icon="🧠", layout="centered")

# CSS වලින් Background එක සහ Fonts ලස්සන කිරීම
st.markdown("""
    <style>
    .main { background-color: #f5f7f8; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_style_with_html=True)

st.title("🧠 AI Smart Predictor Web App")
st.write("ඔබගේ Unique Streamlit ඇප් එක සාර්ථකව වැඩ කරයි! 🎉")

# සරල ගණනය කිරීමක් කරන App එකක්
st.subheader("📊 සරල සංඛ්‍යා ලේඛන ගණකය")
num1 = st.number_input("පළමු සංඛ්‍යාව ඇතුලත් කරන්න:", value=10)
num2 = st.number_input("දෙවන සංඛ්‍යාව ඇතුලත් කරන්න:", value=5)

if st.button("ගණනය කරන්න"):
    ekතුව = num1 + num2
    gunithaya = num1 * num2
    st.success(f"🔢 සංඛ්‍යා දෙකෙහි එකතුව: {ekතුව}")
    st.info(f"✖️ සංඛ්‍යා දෙකෙහි ගුණිතය: {gunithaya}")
