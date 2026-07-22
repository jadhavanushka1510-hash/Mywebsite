import streamlit as st

st.title("contact")

name = st.text_input("Name")

email = st.text_input("Email")

message = st.text_area("Hello, I want to know more about your services.")

if st.button("Send"):
    st.success("Message Sent Successfully")