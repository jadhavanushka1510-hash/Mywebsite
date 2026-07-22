import streamlit as st
from database.database import conn, cursor

st.set_page_config(page_title="Login", page_icon="🔑", layout="centered")

st.title("🔑 Login")

# ---------------- Session Init ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- Inputs ----------------
email = st.text_input("📧 Email")
password = st.text_input("🔒 Password", type="password")

# ---------------- Login Button ----------------
if st.button("Login"):

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        st.session_state.logged_in = True
        st.session_state.username = user[1]

        st.success(f"🎉 Welcome {user[1]}!")

        # 🔥 AUTO REDIRECT TO HOME
        st.switch_page("app.py")

    else:
        st.error("❌ Invalid Email or Password")