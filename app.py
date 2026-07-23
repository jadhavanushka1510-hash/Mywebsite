import streamlit as st

# ---------------- Page Settings ----------------
st.set_page_config(
    page_title="ShopEasy",
    page_icon="🛒",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- HEADER ----------------
st.title("🛒 ShopEasy")
st.write("### Welcome to ShopEasy - Your Online Shopping Destination")

# ---------------- LOGIN STATUS ----------------
if st.session_state.logged_in:
    st.success(f"👋 Welcome {st.session_state.username}")
else:
    st.warning("⚠️ You are not logged in")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🧭 Menu")

# ---------------- LOGOUT BUTTON ----------------
if st.session_state.logged_in:
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

st.sidebar.markdown("---")

# ---------------- NAVIGATION ----------------
if st.sidebar.button("🏠 Home"):
    st.rerun()

if st.sidebar.button("🛍️ Products"):
    st.switch_page("pages/products.py")

if st.sidebar.button("🛒 Cart"):
    st.switch_page("pages/cart.py")

if st.sidebar.button("💳 Checkout"):
    st.switch_page("pages/checkout.py")

if st.sidebar.button("🔑 Login"):
    st.switch_page("pages/login.py")

if st.sidebar.button("📝 Signup"):
    st.switch_page("pages/signup.py")

if st.sidebar.button("🎯 Recommendations"):
    st.switch_page("pages/recommendation.py")

# ---------------- BANNER ----------------
st.image("images/HP laptop.jpg", use_container_width=True)

st.markdown("---")

# ---------------- CATEGORIES ----------------
st.subheader("📂 Categories")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("💻 Electronics")

with col2:
    st.success("📱 Mobiles")

with col3:
    st.success("🎧 Accessories")

st.markdown("---")

# ---------------- FEATURED PRODUCTS ----------------
st.subheader("🔥 Featured Products")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/HP laptop.jpg", use_container_width=True)
    st.write("### HP Laptop")
    st.write("₹55,999")
    st.button("Add to Cart", key="laptop")

with col2:
    st.image("images/boat headphone.jpg", use_container_width=True)
    st.write("### Boat Headphone")
    st.write("₹1,999")
    st.button("Add to Cart", key="headphone")

with col3:
    st.image("images/samsung Galaxy S24.jpg", use_container_width=True)
    st.write("### Samsung Galaxy S24")
    st.write("₹24,999")
    st.button("Add to Cart", key="phone")

st.markdown("---")

# ---------------- FOOTER ----------------
st.write("© 2026 ShopEasy | Made with ❤️ using Streamlit")