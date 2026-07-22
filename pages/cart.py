import streamlit as st
from database.database import conn, cursor

st.set_page_config(
    page_title="Cart",
    page_icon="🛒",
    layout="wide"
)

# ---------------- Login Check ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("⚠️ Please Login First")
    st.stop()

# ---------------- Sidebar ----------------
st.sidebar.success(f"👋 Welcome {st.session_state.username}")

# ---------------- Title ----------------
st.title("🛒 Shopping Cart")
st.write("### Your Selected Products")

# ---------------- Load Cart From Database ----------------
cursor.execute("SELECT * FROM cart")
cart_items = cursor.fetchall()

if len(cart_items) == 0:
    st.info("🛍️ Your cart is currently empty.")

else:
    total = 0

    for item in cart_items:

        with st.container(border=True):

            col1, col2, col3 = st.columns([1, 3, 1])

            with col1:
                st.image(item[4], width=120)

            with col2:
                st.subheader(item[2])
                st.write(f"💰 Price : ₹{item[3]:,}")

            with col3:
                if st.button("❌ Remove", key=f"remove_{item[0]}"):
                    cursor.execute("DELETE FROM cart WHERE id = ?", (item[0],))
                    conn.commit()
                    st.success("✅ Product Removed Successfully")
                    st.rerun()

            total += item[3]

            st.divider()

    st.markdown("---")
    st.subheader(f"🧾 Total Amount : ₹{total:,}")

# ---------------- Buttons ----------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🗑️ Empty Cart", use_container_width=True):
        cursor.execute("DELETE FROM cart")
        conn.commit()
        st.success("✅ Cart Cleared Successfully")
        st.rerun()

with col2:
    if st.button("⬅️ Continue Shopping", use_container_width=True):
        st.switch_page("pages/Products.py")

with col3:
    if len(cart_items) > 0:
        if st.button("💳 Proceed to Checkout", use_container_width=True):
            st.switch_page("pages/Checkout.py")