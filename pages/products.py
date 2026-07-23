import streamlit as st
from database.database import conn, cursor
import os


st.set_page_config(
    page_title="Products",
    page_icon="🛍️",
    layout="wide"
)


# ---------------- LOGIN CHECK ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:
    st.warning("⚠️ Please Login First")
    st.stop()



# ---------------- WISHLIST ----------------

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []



# ---------------- TITLE ----------------

st.title("🛍️ Our Products")
st.write("Browse our latest collection")



# ---------------- CATEGORY ----------------

st.subheader("📂 Select Category")


category = st.selectbox(
    "Choose Category",
    [
        "All",
        "Electronic Devices",
        "Men",
        "Women"
    ],
    key="category_select"
)



# ---------------- SEARCH ----------------

search = st.text_input(
    "🔍 Search Products",
    key="product_search"
)



# ---------------- IMAGE PATH ----------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "images"
)



# ---------------- LOAD PRODUCTS ----------------

cursor.execute(
    "SELECT * FROM products"
)

rows = cursor.fetchall()


products = []


for row in rows:

    image_name = os.path.basename(row[7])


    image_path = os.path.join(
        IMAGE_FOLDER,
        image_name
    )


    if not os.path.exists(image_path):
        image_path = None



    products.append({

        "id": row[0],
        "name": row[1],
        "category": row[2],
        "price": row[3],
        "old_price": row[4],
        "discount": row[5],
        "stock": row[6],
        "image": image_path,
        "rating": row[8]

    })



# ---------------- SEARCH FILTER ----------------

if search:

    products = [

        p for p in products

        if search.lower() in p["name"].lower()

    ]



# ---------------- CATEGORY FILTER ----------------


if category == "Electronic Devices":

    electronics = [
"HP Laptop",
        "DELL Laptop",
        "Samsung Galaxy S24",
        "iPhone 16 Pro Max",
        "Boat Headphones",
        "Sony Headphones",
        "Gaming Keyboard",
        "Logitech Keyboard",
        "Dell Mouse",
        "Dell Mouse 2"
    ]


    products = [

        p for p in products

        if p["name"].lower() in
        [x.lower() for x in electronics]

    ]



elif category == "Men":

    men = [

        "Nike Shoes",
        "Levi's T-Shirt",
        "Nike T-Shirt",
        "Noise Watch",
        "Fire-Boltt Watch",
        "American Tourister Bag",

    ]


    products = [

        p for p in products

        if p["name"].lower() in
        [x.lower() for x in men]

    ]



elif category == "Women":

    women = [
        "American Tourister Bag",
        "Noise Watch",
        "Fire-Boltt Watch",
        "Levi's T-Shirt",
        "Nike T-Shirt",
        "Nike Shoes",
        "Puma Shoes",
        "Wildcarft bag",

    ]


    products = [

        p for p in products

        if p["name"].lower() in
        [x.lower() for x in women]

    ]



st.write(
    f"### Showing {len(products)} Products"
)
# ---------------- PRODUCT CARDS ----------------

cols = st.columns(3)


for i, product in enumerate(products):

    with cols[i % 3]:

        with st.container(border=True):


            # IMAGE

            if product["image"]:

                st.image(
                    product["image"],
                    use_container_width=True
                )

            else:

                st.warning(
                    "Image not found"
                )



            st.subheader(
                product["name"]
            )



            st.write(
                "⭐ Rating:",
                product["rating"]
            )



            st.markdown(
                f"~~₹{product['old_price']:,}~~"
            )


            st.markdown(
                f"## ₹{product['price']:,}"
            )


            st.success(
                product["discount"]
            )


            st.info(
                product["stock"]
            )



            c1, c2 = st.columns(2)



            # -------- CART --------

            with c1:

                if st.button(
                    "🛒 Add To Cart",
                    key=f"cart_{i}"
                ):


                    cursor.execute(
                    """
                    INSERT INTO cart
                    (product_id, product_name, price, image)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        product["id"],
                        product["name"],
                        product["price"],
                        product["image"]
                    ))


                    conn.commit()


                    st.success(
                        "Added To Cart"
                    )



            # -------- WISHLIST --------

            with c2:


                if st.button(
                    "❤️ Wishlist",
                    key=f"wish_{i}"
                ):


                    st.session_state.wishlist.append(
                        product
                    )


                    st.success(
                        "Added To Wishlist"
                    )



            st.markdown("---")



# ---------------- COUNTS ----------------


st.markdown("---")


cursor.execute(
    "SELECT COUNT(*) FROM cart"
)


cart_count = cursor.fetchone()[0]


st.write(
    f"🛒 Cart Items : **{cart_count}**"
)


st.write(
    f"❤️ Wishlist Items : **{len(st.session_state.wishlist)}**"
)