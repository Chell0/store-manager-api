"""Create tables in the PostgreSQL database."""
users = """
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin boolean
)
"""
category = """
CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) UNIQUE NOT NULL
)
"""

products = """
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL UNIQUE,
    stock INTEGER NOT NULL,
    price INTEGER NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (category_name) REFERENCES category (category_name) 
)
"""

sales = """
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (product_name) REFERENCES products (product_name),
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
)
"""

queries = [users, category, products, sales]
