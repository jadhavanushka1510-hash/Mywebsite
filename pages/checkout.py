import streamlit as st
from database.database import conn, cursor

st.set_page_config(
    page_title="Checkout",
    page_icon="💳",
    layout="wide"
)

# ---------------- Login Check ----------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please Login First")
    st.stop()

st.sidebar.success(f"👋 Welcome {st.session_state.username}")

st.title("💳 Checkout")

# ---------------- Load Cart ----------------
cursor.execute("SELECT * FROM cart")
cart_items = cursor.fetchall()

if len(cart_items) == 0:
    st.warning("🛒 Your cart is empty.")
    st.stop()

# ---------------- Total Calculation ----------------
total = sum(item[3] for item in cart_items)

st.subheader(f"🧾 Total Amount: ₹{total:,}")

st.markdown("---")

# ---------------- Customer Details ----------------
st.subheader("📦 Delivery Details")

name = st.text_input("👤 Full Name")
mobile = st.text_input("📞 Mobile Number")
address = st.text_area("🏠 Delivery Address")
city = st.text_input("🏙️ City")
pincode = st.text_input("📮 Pincode")

payment = st.selectbox(
    "💳 Payment Method",
    ["Cash on Delivery", "UPI", "Credit Card", "Debit Card"]
)

st.markdown("---")

# ---------------- Place Order ----------------
if st.button("✅ Place Order"):

    if not name or not mobile or not address or not city or not pincode:
        st.error("❌ Please fill all details.")
    else:

        # ✅ SAVE ORDER IN DATABASE (IMPORTANT FIX)
        cursor.execute("""
        INSERT INTO orders(
            username,
            customer_name,
            phone,
            address,
            city,
            pincode,
            total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            st.session_state.username,
            name,
            mobile,
            address,
            city,
            pincode,
            total
        ))

        conn.commit()

        # 🛒 Clear Cart
        cursor.execute("DELETE FROM cart")
        conn.commit()

        st.success("🎉 Order Placed Successfully!")
        st.balloons()

        st.info("📦 Thank you for your order!")