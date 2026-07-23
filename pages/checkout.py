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

# ---------------- Total ----------------
total = sum(item[3] for item in cart_items)

st.subheader(f"🧾 Total Amount : ₹{total:,}")

st.markdown("---")

st.subheader("📦 Delivery Details")

name = st.text_input("👤 Full Name")
mobile = st.text_input("📞 Mobile Number")
address = st.text_area("🏠 Delivery Address")
city = st.text_input("🏙️ City")
pincode = st.text_input("📮 Pincode")

payment = st.selectbox(
    "💳 Payment Method",
    [
        "Cash on Delivery",
        "UPI",
        "Credit Card",
        "Debit Card"
    ]
)

st.markdown("---")

if st.button("🛍️ Place Order", use_container_width=True):

    if not name or not mobile or not address or not city or not pincode:
        st.error("❌ Please fill all details.")

    else:

        cursor.execute("""
        INSERT INTO orders
        (
            username,
            customer_name,
            phone,
            address,
            city,
            pincode,
            total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            st.session_state.username,
            name,
            mobile,
            address,
            city,
            pincode,
            total
        ))

        conn.commit()

        # Empty Cart
        cursor.execute("DELETE FROM cart")
        conn.commit()

        st.balloons()

        st.success("🎉 Order Placed Successfully!")

        st.markdown("## ✅ Order Confirmation")

        st.write(f"**Customer:** {name}")
        st.write(f"**Mobile:** {mobile}")
        st.write(f"**Address:** {address}")
        st.write(f"**City:** {city}")
        st.write(f"**Pincode:** {pincode}")
        st.write(f"**Payment:** {payment}")
        st.write(f"**Total Paid:** ₹{total:,}")

        st.info("🚚 Your order will be delivered within 3-5 working days.")

        st.success("🙏 Thank You For Shopping With ShopEasy!")

        if st.button("🏠 Back To Home"):
            st.switch_page("app.py")