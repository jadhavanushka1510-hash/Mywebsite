import streamlit as st
from database.database import conn, cursor

st.set_page_config(
    page_title="Admin Panel",
    page_icon="📊",
    layout="wide"
)

st.title("📊 All Orders (Admin Panel)")

search = st.text_input("🔍 Search by Name or Phone")

if search:
    cursor.execute("""
        SELECT * FROM orders
        WHERE customer_name LIKE ? OR phone LIKE ?
    """, (f"%{search}%", f"%{search}%"))
else:
    cursor.execute("SELECT * FROM orders")

orders = cursor.fetchall()

if not orders:
    st.info("No orders yet.")

else:
    for order in orders:

        with st.container():

            st.markdown("### 📦 Order Details")

            st.write(f"👤 User: {order[1]}")
            st.write(f"📦 Customer: {order[2]}")
            st.write(f"📞 Phone: {order[3]}")
            st.write(f"🏠 Address: {order[4]}, {order[5]} - {order[6]}")
            st.write(f"💰 Total: ₹{order[7]}")

            # Status
            status = order[8] if len(order) > 8 else "Pending"
            st.write(f"📌 Status: {status}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("🗑️ Delete", key=f"del_{order[0]}"):
                    cursor.execute(
                        "DELETE FROM orders WHERE id=?",
                        (order[0],)
                    )
                    conn.commit()
                    st.success("Order deleted.")
                    st.rerun()

            with col2:
                if st.button("✔ Delivered", key=f"done_{order[0]}"):

                    if len(order) > 8:
                        cursor.execute(
                            "UPDATE orders SET status=? WHERE id=?",
                            ("Delivered", order[0])
                        )
                        conn.commit()
                        st.success("Order marked as Delivered.")
                    else:
                        st.warning("Status column database मध्ये नाही.")

                    st.rerun()

            st.markdown("---")