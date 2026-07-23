import streamlit as st
import os

st.set_page_config(
    page_title="Amazon Clone",
    page_icon="🛒",
    layout="wide"
)

# ---------------- IMAGE PATH ----------------

BASE_DIR = r"C:\Users\ANUSHKA\OneDrive\Desktop\Mywebsite"
IMAGE_DIR = os.path.join(BASE_DIR, "images")


def img(name):
    return os.path.join(IMAGE_DIR, name)



# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""



# ---------------- SIDEBAR ----------------

st.sidebar.title("🛒 Amazon Clone")


if st.session_state.logged_in:
    st.sidebar.success(
        f"👋 Welcome {st.session_state.username}"
    )

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

else:
    st.sidebar.warning("⚠️ Please Login or Signup")



# ---------------- HOME ----------------

st.title("🛒 Amazon Clone")
st.write("Welcome to our Online Shopping Store")

st.markdown("---")



# ---------------- CATEGORY ----------------

st.markdown("## 📂 Shop by Category")


c1,c2,c3,c4,c5 = st.columns(5)


with c1:
    st.image(img("HP laptop.jpg"), use_container_width=True)
    st.caption("💻 Laptop")


with c2:
    st.image(img("Iphone 16 por max.jpg"), use_container_width=True)
    st.caption("📱 Mobile")


with c3:
    st.image(img("boat headphone.jpg"), use_container_width=True)
    st.caption("🎧 Headphone")


with c4:
    st.image(img("Fire-Boltt Watch.jpg"), use_container_width=True)
    st.caption("⌚ Watch")


with c5:
    st.image(img("Sony headphone.jpg"), use_container_width=True)
    st.caption("📷 Camera")



c6,c7,c8,c9,c10 = st.columns(5)


with c6:
    st.image(img("Gaming keyboard.jpg"), use_container_width=True)
    st.caption("⌨️ Keyboard")


with c7:
    st.image(img("Dell Mouse.jpg"), use_container_width=True)
    st.caption("🖱️ Mouse")


with c8:
    st.image(img("Nike Shoes.jpg"), use_container_width=True)
    st.caption("👟 Shoes")


with c9:
    st.image(img("Levi's T-Shirt.jpg"), use_container_width=True)
    st.caption("👕 T-Shirt")


with c10:
    st.image(img("American Tourister Bag.jpg"), use_container_width=True)
    st.caption("👜 Bag")


st.markdown("---")

# ---------------- TODAY'S DEALS ----------------

st.markdown("## 🔥 Today's Deals")

col1, col2, col3 = st.columns(3)


with col1:
    st.image(img("Iphone 16 por max.jpg"), use_container_width=True)
    st.subheader("iPhone 16 Pro Max")
    st.write("⭐⭐⭐⭐⭐")
    st.success("₹79,999")


with col2:
    st.image(img("HP laptop.jpg"), use_container_width=True)
    st.subheader("HP Laptop")
    st.write("⭐⭐⭐⭐⭐")
    st.success("₹55,999")


with col3:
    st.image(img("boat headphone.jpg"), use_container_width=True)
    st.subheader("Boat Headphones")
    st.write("⭐⭐⭐⭐")
    st.success("₹1,999")



st.markdown("---")



# ---------------- FEATURED PRODUCTS ----------------

st.markdown("## ⭐ Featured Products")


f1, f2, f3 = st.columns(3)


with f1:
    st.image(img("Fire-Boltt Watch.jpg"), use_container_width=True)
    st.subheader("Smart Watch")
    st.write("₹3,999")


with f2:
    st.image(img("Nike Shoes.jpg"), use_container_width=True)
    st.subheader("Nike Shoes")
    st.write("₹2,999")


with f3:
    st.image(img("Wildcraft bag.jpg"), use_container_width=True)
    st.subheader("Hand Bag")
    st.write("₹1,499")



st.markdown("---")



# ---------------- TOP BRANDS ----------------

st.markdown("## 🏆 Top Brands")


b1,b2,b3,b4,b5 = st.columns(5)


with b1:
    st.info("🍎 Apple")

with b2:
    st.info("📱 Samsung")

with b3:
    st.info("💻 HP")

with b4:
    st.info("🎧 Boat")

with b5:
    st.info("⌨️ Logitech")



st.markdown("---")



# ---------------- CUSTOMER REVIEWS ----------------

st.markdown("## ⭐ Customer Reviews")


r1,r2,r3 = st.columns(3)


with r1:
    st.success("⭐⭐⭐⭐⭐")
    st.write("Excellent Product")
    st.caption("Very good quality and fast delivery.")


with r2:
    st.success("⭐⭐⭐⭐")
    st.write("Fast Delivery")
    st.caption("Received my order within 2 days.")


with r3:
    st.success("⭐⭐⭐⭐⭐")
    st.write("Best Quality")
    st.caption("Worth buying. Highly recommended.")



st.markdown("---")


st.info("👉 Open Products page from the left sidebar to browse all products.")



st.markdown("---")



# ---------------- FOOTER ----------------

st.markdown("""
<center>

## 🛒 Amazon Clone

📧 support@gmail.com

📞 +91 9876543210

© 2026 All Rights Reserved

</center>
""", unsafe_allow_html=True)