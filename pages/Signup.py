import streamlit as st
from database.database import conn, cursor

st.set_page_config(page_title="Signup", page_icon="📝")

st.title("📝 Create New Account")

username = st.text_input("👤 Username")
email = st.text_input("📧 Email")
password = st.text_input("🔒 Password", type="password")

if st.button("Signup"):

    if username == "" or email == "" or password == "":
        st.error("Please fill all fields.")

    else:
        try:
            cursor.execute("""
            INSERT INTO users(username, email, password)
            VALUES (?, ?, ?)
            """, (username, email, password))

            conn.commit()

            st.success("✅ Account Created Successfully!")
            st.info("Now open the Login page and login.")

        except:
            st.error("Email already exists!")