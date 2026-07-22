import sqlite3

# ---------------- CONNECTION ----------------
conn = sqlite3.connect("database/database.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- PRODUCTS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price INTEGER,
    old_price INTEGER,
    discount TEXT,
    stock TEXT,
    image TEXT,
    rating TEXT
)
""")

# ---------------- CART TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    product_name TEXT,
    price INTEGER,
    image TEXT
)
""")

# ---------------- USERS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

# ---------------- ORDERS TABLE (NEW FIX) ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    customer_name TEXT,
    phone TEXT,
    address TEXT,
    city TEXT,
    pincode TEXT,
    total INTEGER
)
""")

# ---------------- COMMIT ----------------
conn.commit()