from database.database import conn, cursor

# ---------------- DELETE OLD PRODUCTS ----------------

cursor.execute("DELETE FROM products")


# ---------------- PRODUCTS DATA ----------------

products = [

(
"Nike Air Shoes",
"Shoes",
2999,
4999,
"40% OFF",
"In Stock",
"images/shoes.jpg",
4.5
),

(
"Puma T-Shirt",
"T-Shirt",
1499,
2499,
"30% OFF",
"In Stock",
"images/tshirt.jpg",
4.3
),

(
"Iphone",
"Phone",
19999,
24999,
"20% OFF",
"In Stock",
"images/phone.webp",
4.6
),

(
"HP Laptop",
"Laptop",
55000,
65000,
"15% OFF",
"In Stock",
"images/laptop.jpg",
4.7
),

(
"Leather Bag",
"Bag",
2499,
3999,
"35% OFF",
"In Stock",
"images/bag.jpg",
4.4
)

]

# ---------------- INSERT QUERY ----------------

for product in products:

    cursor.execute(
        """
        INSERT INTO products
        (
        name,
        category,
        price,
        old_price,
        discount,
        stock,
        image,
        rating
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        product
    )


conn.commit()

print("✅ New Products inserted successfully!")

conn.close()