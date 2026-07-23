from database import cursor, conn

# ---------------- DELETE OLD PRODUCTS ----------------
cursor.execute("DELETE FROM products")

# ---------------- PRODUCTS DATA ----------------
products = [
    (
        "HP Laptop",
        "Laptop",
        55999,
        62999,
        "11% OFF",
        "In Stock",
        "images/HP laptop.jpg",
        "⭐⭐⭐⭐⭐"
    ),
    (
        "Samsung Galaxy S24",
        "Phone",
        24999,
        28999,
        "14% OFF",
        "In Stock",
        "images/samsung Galaxy S24.jpg",
        "⭐⭐⭐⭐"
    ),
    (
        "Boat Headphone",
        "Headphone",
        1999,
        2499,
        "20% OFF",
        "In Stock",
        "images/boat headphone.jpg",
        "⭐⭐⭐⭐"
    ),
    (
        "Noise Watch",
        "Watch",
        3999,
        4999,
        "20% OFF",
        "In Stock",
        "images/Noise watch.jpg",
        "⭐⭐⭐⭐⭐"
    ),
    (
        "Nike Shoes",
        "Shoes",
        2999,
        3799,
        "21% OFF",
        "In Stock",
        "images/Nike Shoes.jpg",
        "⭐⭐⭐⭐"
    ),
    (
        "American Tourister Bag",
        "Bag",
        1499,
        1999,
        "25% OFF",
        "In Stock",
        "images/American Tourister Bag.jpg",
        "⭐⭐⭐⭐"
    ),
    (
        "DELL Laptop",
        "Laptop",
        45999,
        52999,
        "13% OFF",
        "In Stock",
        "images/DELL laptop.jpg",
        "⭐⭐⭐⭐⭐"
    ),
    (
        "Gaming Keyboard",
        "Keyboard",
        2199,
        2799,
        "21% OFF",
        "In Stock",
        "images/Gaming keyboard.jpg",
        "⭐⭐⭐⭐"
    ),
    (
        "Dell Mouse",
        "Mouse",
        999,
        1299,
        "23% OFF",
        "In Stock",
        "images/Dell Mouse.jpg",
        "⭐⭐⭐⭐⭐"
    ),
    (
        "Levi's T-Shirt",
        "T-Shirt",
        699,
        999,
        "30% OFF",
        "In Stock",
        "images/Levi's T-Shirt.jpg",
        "⭐⭐⭐⭐⭐"
    )
]

# ---------------- INSERT PRODUCTS ----------------
cursor.executemany("""
INSERT INTO products
(name, category, price, old_price, discount, stock, image, rating)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", products)

conn.commit()

print("✅ Products inserted successfully!")