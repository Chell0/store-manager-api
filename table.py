"""Create tables in the PostgreSQL database."""
users = """
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin boolean NOT NULL
)
"""
category = """
CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL,
)
"""

products = """
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock INTEGER NOT NULL,
    price INTEGER NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (category_name) REFERENCES category (category_name) ON UPDATE CASCADE ON DELETE CASCADE
)
"""

sales = """
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (product_name) REFERENCES products (product_name) ON UPDATE CASCADE ON DELTED CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE
)
"""

queries = [users, category, products, sales]
