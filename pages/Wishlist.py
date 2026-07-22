import streamlit as st

st.set_page_config(
    page_title="Wishlist",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ My Wishlist")

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if len(st.session_state.wishlist) == 0:
    st.info("Your wishlist is empty.")
else:

    cols = st.columns(3)

    for i, product in enumerate(st.session_state.wishlist):

        with cols[i % 3]:

            with st.container(border=True):

                st.image(product["image"], use_container_width=True)

                st.subheader(product["name"])

                st.write(product["rating"])

                st.write(f"### {product['price']}")

                if st.button("❌ Remove", key=f"remove{i}"):

                    st.session_state.wishlist.pop(i)

                    st.rerun()