import streamlit as st

st.title("🤖 Gen AI Text Generator")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    st.write("Your generated text will appear here.")
