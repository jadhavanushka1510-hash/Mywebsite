from database import cursor, conn

products = [
    ("HP Laptop", "Laptop", 55999, 62999, "11% OFF", "In Stock", "images/laptop.jpg", "⭐⭐⭐⭐⭐"),
    ("Samsung Phone", "Phone", 24999, 28999, "14% OFF", "In Stock", "images/phone.webp", "⭐⭐⭐⭐"),
    ("Boat Headphones", "Headphone", 1999, 2499, "20% OFF", "In Stock", "images/headphone.jpg", "⭐⭐⭐⭐"),
    ("Smart Watch", "Watch", 3999, 4999, "20% OFF", "In Stock", "images/watch.jpg", "⭐⭐⭐⭐⭐"),
    ("Nike Shoes", "Shoes", 2999, 3799, "21% OFF", "In Stock", "images/shoes.jpg", "⭐⭐⭐⭐"),

    ("Leather Bag", "Bag", 1499, 1999, "25% OFF", "In Stock", "images/bag.jpg", "⭐⭐⭐⭐"),
    ("Canon Camera", "Camera", 45999, 52999, "13% OFF", "In Stock", "images/camera.jpg", "⭐⭐⭐⭐⭐"),
    ("Gaming Keyboard", "Keyboard", 2199, 2799, "21% OFF", "In Stock", "images/keyboard.jpg", "⭐⭐⭐⭐"),
    ("Wireless Mouse", "Mouse", 999, 1299, "23% OFF", "In Stock", "images/mouse.jpg", "⭐⭐⭐⭐⭐"),
    ("T-Shirt", "T-Shirt", 699, 999, "30% OFF", "In Stock", "images/tshirt.jpg", "⭐⭐⭐⭐⭐")
]

cursor.executemany("""
INSERT INTO products(name, category, price, old_price, discount, stock, image, rating)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", products)

conn.commit()

print("Products inserted successfully!")