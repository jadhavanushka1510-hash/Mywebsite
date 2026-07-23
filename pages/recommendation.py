import streamlit as st
import pandas as pd
import os
from database.database import conn, cursor


st.set_page_config(
    page_title="Recommendations",
    page_icon="🎯",
    layout="wide"
)


st.title("🎯 Smart Shopping Recommendation System")
st.write("Select category to see products.")


# ---------------- IMAGE PATH ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "images"
)



# ---------------- PRODUCT DATA ----------------

products = pd.DataFrame({

    "Product":[
        "HP Laptop",
        "DELL Laptop",
        "Samsung Galaxy S24",
        "iPhone 16 Pro Max",
        "Boat Headphones",
        "Sony Headphones",
        "Noise Watch",
        "Fire-Boltt Watch",
        "Nike Shoes",
        "Puma Shoes",
        "Levi's T-Shirt",
        "Nike T-Shirt",
        "American Tourister Bag",
        "Wildcraft Bag",
        "Gaming Keyboard",
        "Logitech Keyboard",
        "Dell Mouse",
        "Dell Mouse 2"
    ],


    "Price":[
        55999,
        62999,
        24999,
        139999,
        1999,
        2999,
        3999,
        3499,
        2999,
        3499,
        699,
        999,
        1499,
        1899,
        2199,
        2499,
        999,
        1199
    ],


    "Image":[
        "HP laptop.jpg",
        "DELL laptop.jpg",
        "samsung Galaxy S24.jpg",
        "Iphone 16 por max.jpg",
        "boat headphone.jpg",
        "Sony headphone.jpg",
        "Noise watch.jpg",
        "Fire-Boltt Watch.jpg",
        "Nike Shoes.jpg",
        "Puma shoes.jpg",
        "Levi's T-Shirt.jpg",
        "Nike tshirt.jpg",
        "American Tourister Bag.jpg",
        "Wildcraft bag.jpg",
        "Gaming keyboard.jpg",
        "Logitech keyboard.jpg",
        "Dell Mouse.jpg",
        "Dell mouse (2).jpg"
    ]

})


# ---------------- CATEGORY ----------------

st.subheader("🔍 Search Recommendation")


selected_category = st.selectbox(

    "Select Category",

    [
        "Electronic Devices",
        "Men",
        "Women"
    ]

)



category_products = {


    "Electronic Devices":[
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
    ],


    "Men":[
        "Nike Shoes",
        "Levi's T-Shirt",
        "Nike T-Shirt",
        "Noise Watch",
        "Fire-Boltt Watch",
        "American Tourister Bag",
        
    ],


    "Women":[
        "American Tourister Bag",
        "Noise Watch",
        "Fire-Boltt Watch",
        "Levi's T-Shirt",
        "Nike T-Shirt",
        "Nike Shoes",
        "Puma Shoes",
        "Wildcarft bag",
    ]

}


# show selected category products

recommended_names = category_products[selected_category]

# ---------------- SHOW PRODUCTS ----------------


st.markdown("---")


st.subheader(
    f"🛍️ {selected_category} Products"
)



recommended = products[
    products["Product"].isin(recommended_names)
]



cols = st.columns(2)



for index, (_, row) in enumerate(recommended.iterrows()):


    with cols[index % 2]:


        image_path = os.path.join(
            IMAGE_FOLDER,
            row["Image"]
        )


        if os.path.exists(image_path):

            st.image(
                image_path,
                width=220
            )

        else:

            st.warning(
                "Image not found"
            )



        st.markdown(
            f"### 🛍️ {row['Product']}"
        )


        st.write(
            f"💰 Price : ₹{row['Price']:,}"
        )



        c1, c2 = st.columns(2)



        # ---------------- ADD TO CART ----------------


        with c1:


            if st.button(
                "🛒 Add To Cart",
                key=f"cart_{row['Product']}"
            ):


                cursor.execute(

                    """
                    INSERT INTO cart
                    (product_id, product_name, price, image)
                    VALUES (?, ?, ?, ?)
                    """,

                    (
                        0,
                        row["Product"],
                        row["Price"],
                        image_path
                    )

                )


                conn.commit()


                st.success(
                    "✅ Added To Cart"
                )



        # ---------------- BUY NOW ----------------


        with c2:


            if st.button(
                "⚡ Buy Now",
                key=f"buy_{row['Product']}"
            ):


                cursor.execute(
                    "DELETE FROM cart"
                )



                cursor.execute(

                    """
                    INSERT INTO cart
                    (product_id, product_name, price, image)
                    VALUES (?, ?, ?, ?)
                    """,

                    (
                        0,
                        row["Product"],
                        row["Price"],
                        image_path
                    )

                )


                conn.commit()



                st.switch_page(
                    "pages/Checkout.py"
                )


        st.markdown("---")