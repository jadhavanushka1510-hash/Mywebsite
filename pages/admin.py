import streamlit as st
from database.database import conn, cursor

st.set_page_config(page_title="Admin Panel", page_icon="📊", layout="wide")

st.title("📊 All Orders (Admin Panel)")

# ---------------- SEARCH ----------------
search = st.text_input("🔍 Search by Name or Phone")

# ---------------- QUERY ----------------
if search:
    cursor.execute("""
        SELECT * FROM orders 
        WHERE customer_name LIKE ? OR phone LIKE ?
    """, (f"%{search}%", f"%{search}%"))
else:
    cursor.execute("SELECT * FROM orders")

orders = cursor.fetchall()

# ---------------- EMPTY CHECK ----------------
if not orders:
    st.info("No orders yet.")
else:
    for order in orders:
        with st.container():
            st.markdown("### 📦 Order Details")

            st.write(f"👤 User: {order[1]}")
            st.write(f"📦 Name: {order[2]}")
            st.write(f"📞 Phone: {order[3]}")
            st.write(f"🏠 Address: {order[4]}, {order[5]} - {order[6]}")
            st.write(f"💰 Total: ₹{order[7]}")
            st.write(f"📌 Status: {order[8]}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑️ Delete", key=f"del_{order[0]}"):
                    cursor.execute("DELETE FROM orders WHERE id=?", (order[0],))
                    conn.commit()
                    st.rerun()

            with col2:
                if st.button(f"✔ Delivered", key=f"done_{order[0]}"):
                    cursor.execute(
                        "UPDATE orders SET status='Delivered' WHERE id=?",
                        (order[0],)
                    )
                    conn.commit()
                    st.rerun()

            st.markdown("---")