import psycopg2

from api.app.v2.db import StoreDb

# Store Model


class StoreModel(StoreDb):
    """This class represents the store model."""

################# CATEGORY SECTION ####################
    
    def __init__(self):
        super().__init()

    Add a category
    def add_category(self, category_name):
        """Add a category."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM category WHERE category_name='%s'
            """ % category_name)
        category_res = cursor.fetchone()
        if category_res:
            return {"message": "A category with {} already exists".format(category_name)}, 409
        else: 
            cursor.execute(
                """
                INSERT INTO category (category_name)
                VALUES ('%s')
                """
                % (category_name)
            )
            connection.commit()
            return category_name
        

    # Fetch all categories
    def get_all_categories(self):
        """Fetch all categories."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM category")
        result = cursor.fetchall()
        return result

    # Fetch one category
    def get_one_category(self, id):
        """Fetch a product by id from the db."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM category WHERE category_id='%s'
            """
            % (id)
        )
        category = cursor.fetchone()
        return category

    # Delete a category
    def delete_a_category(self, category_id):
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        """Delete a category by id."""
        cursor.execute(
            """
            DELETE FROM category WHERE category_id='%s'
            """
            % (category_id)
        )
        connection.commit()
        return {'message': "Category successfuly deleted"}, 200

################# PRODUCT SECTION #####################

    # Add a product
    def product_add(self, data):
        """Add a product."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO products (product_name, stock_quantity, price, category_id)
            VALUES ('%s', '%s', '%s', '%s')
            """
            % (data[0], data[1], data[2], data[3])
        )
        connection.commit()
        return data

    # Fetch all products
    def get_all_products(self):
        """Fetch all products."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        return result

    # Fetch one product
    def get_one_product(self, id):
        """Fetch a product by id from the db."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM products WHERE product_id='%s'
            """
            % (id)
        )
        product_id = cursor.fetchone()
        return product

    def get_product_by_name(self, product_name):
        """Fetch a product by name from the db."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM products WHERE product_name='%s'
            """
            % (product_name)
        )
        product_name = cursor.fetchone()
        return product


    # Update a product
    def modify_a_product(self, stock_quantity):
        """Modify a product."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE products SET stock_quantity='%s' WHERE product_id='%s'
            """
            % (stock_quantity, id)
        )
        product = cursor.update()
        connection.commit()
        return product

    # Delete a product
    def delete_a_product(self, product_id):
        """Delete a product by id,"""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE from products WHERE product_id='%s'
            """
            % (product_id)
        )
        connection.commit()
        return product_id

###################### SALES SECTION ##########################

    # Add a sale order
    def add_sale_order(self, data):
        """Add a sale order."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO sales (sale_id, product_name, quantity, price, user_id)
            VALUES ('%s', '%s', '%s', '%s', '%s')
            """
            % (data['sale_id'], data['product_name'], data['quantity'], data['price'], data['user_id'])
        )
        connect.commit()
        return data

    # Fetch all sales
    def get_all_sales(self):
        """Fetch all sales."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sales")
        result = cursor.fetchall()
        return result

    # Fetch a sale order
    def get_a_sale_order(self, sale_id):
        """Fetch a sale order by id."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sales WHERE sale_id='%s'"
            % (id)
        )
        sale_order = cursor.fetchone()
        return sale_order
