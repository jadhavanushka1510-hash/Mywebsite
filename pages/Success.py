import streamlit as st

st.set_page_config(page_title="Success", page_icon="✅")

st.title("✅ Order Placed Successfully!")

st.success("Your order has been placed successfully.")
st.write("Thank you for shopping with us.")

if st.button("Go to Home"):
    st.switch_page("pages/Home.py")