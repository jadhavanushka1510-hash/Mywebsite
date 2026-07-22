import streamlit as st
from database.database import conn, cursor

st.set_page_config(
    page_title="Products",
    page_icon="🛍️",
    layout="wide"
)

# ---------------- Login Check ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("⚠️ Please Login First")
    st.stop()

# ---------------- Session State ----------------
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# ---------------- Sidebar ----------------
st.sidebar.success(f"👋 Welcome {st.session_state.username}")
st.sidebar.header("📂 Categories")

category = st.sidebar.selectbox(
    "Select Category",
    [
        "All",
        "Laptop",
        "Phone",
        "Headphone",
        "Watch",
        "Shoes",
        "T-Shirt",
        "Bag",
        "Keyboard",
        "Mouse"
    ]
)

# ---------------- Title ----------------
st.title("🛍️ Our Products")
st.write("Browse our latest collection")

# ---------------- Search ----------------
search = st.text_input("🔍 Search Products")

# ---------------- Load Products ----------------
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

products = []

for row in rows:
    products.append({
        "id": row[0],
        "name": row[1],
        "category": row[2],
        "price": f"₹{row[3]:,}",
        "old_price": f"₹{row[4]:,}",
        "discount": row[5],
        "stock": row[6],
        "image": row[7],
        "rating": row[8]
    })

# ---------------- Search ----------------
if search:
    products = [
        p for p in products
        if search.lower() in p["name"].lower()
    ]

# ---------------- Category ----------------
if category != "All":
    products = [
        p for p in products
        if p["category"] == category
    ]

st.write(f"### Showing {len(products)} Products")

cols = st.columns(3)

for i, product in enumerate(products):

    with cols[i % 3]:

        with st.container(border=True):

            st.image(product["image"], use_container_width=True)

            st.subheader(product["name"])

            st.write(product["rating"])

            st.markdown(f"~~{product['old_price']}~~")

            st.markdown(f"### {product['price']}")

            st.success(product["discount"])

            st.info(product["stock"])

            c1, c2 = st.columns(2)

            # ---------------- Add To Cart ----------------
            with c1:

                if st.button("🛒 Add to Cart", key=f"cart{i}"):

                    price = int(product["price"].replace("₹", "").replace(",", ""))

                    cursor.execute("""
                    INSERT INTO cart(product_id, product_name, price, image)
                    VALUES (?, ?, ?, ?)
                    """, (
                        product["id"],
                        product["name"],
                        price,
                        product["image"]
                    ))

                    conn.commit()

                    st.success("✅ Added To Cart")

            # ---------------- Wishlist ----------------
            with c2:

                if st.button("❤️ Wishlist", key=f"wish{i}"):

                    st.session_state.wishlist.append(product)

                    st.success("❤️ Added To Wishlist")

st.markdown("---")

# ---------------- Cart Count ----------------
cursor.execute("SELECT COUNT(*) FROM cart")
cart_count = cursor.fetchone()[0]

st.write(f"🛒 Cart Items : **{cart_count}**")
st.write(f"❤️ Wishlist Items : **{len(st.session_state.wishlist)}**")