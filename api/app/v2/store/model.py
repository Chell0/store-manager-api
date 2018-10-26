from api.app.v2.db import StoreDb

# Store Model


class StoreModel(StoreDb):
    """This class represents the products model."""

################# CATEGORY SECTION ####################

    # Add a category
    store = StoreModel()
    store.product_add()

    def add_category(self, data):
        """Add a category."""
        self.cursor.execute(
            """
            INSERT INTO category (category_id, category_name)
            VALUES ('%s', '%s')
            """
            % (data['category_id'], data['category_name'])
        )
        # self.store(....)
        return data

    # Fetch all categories
    def get_all_categories(self):
        """Fetch all categories."""
        self.cursor.execute("SELECT * FROM category")
        result = self.cursor.fetchall()
        return result

    # Fetch one category
    def get_one_category(self, id):
        """Fetch a product by id from the db."""
        self.cursor.execute(
            """
            SELECT * FROM sales WHERE category_id='%s'
            """
            % (id)
        )
        category = self.cursor.fetchone()
        return category

    # Delete a category
    def delete_a_category(self, category_id):
        """Delete a category by id."""
        self.cursor.execute(
            """
            DELETE from category WHERE category_id='%s'
            """
            % (category_id)
        )
        self.connection.commit()
        return category_id

################# PRODUCT SECTION #####################

    # Add a product
    def product_add(self, data):
        """Add a product."""
        self.cursor.execute(
            """
            INSERT INTO products (product_name, stock, price, category_name)
            VALUES ('%s', '%s', '%s', '%s')
            """
            % (data['product_name'], data['stock'], data['price'], data['category_name'])
        )
        self.store()

        # self.connection.commit()
        return data

    # Fetch all products
    def get_all_products(self):
        """Fetch all products."""
        self.cursor.execute("SELECT * FROM products")
        result = self.cursor.fetchall()
        return result

    # Fetch one product
    def get_one_product(self, id):
        """Fetch a product by id from the db."""
        self.cursor.execute(
            """
            SELECT * FROM products WHERE product_id='%s'
            """
            % (id)
        )
        product = self.cursor.fetchone()
        return product

    # Update a product
    def modify_a_product(self, id, stock):
        """Modify a product."""
        self.cursor.execute(
            """
            UPDATE products SET stock='%s' WHERE product_id='%s'
            """
            % (stock, id)
        )
        self.connection.commit()

    # Delete a product
    def delete_a_product(self, product_id):
        """Delete a product by id,"""
        self.cursor.execute(
            """
            DELETE from products WHERE product_id='%s'
            """
            % (product_id)
        )
        self.connection.commit()
        return product_id

###################### SALES SECTION ##########################

    # Add a sale order
    def add_sale_order(self, data):
        """Add a sale order."""
        self.cursor.execute(
            """
            INSERT INTO sales (sale_id, product_name, quantity, price, user_id)
            VALUES ('%s', '%s', '%s', '%s', '%s')
            """
            % (data['sale_id'], data['product_name'], data['quantity'], data['price']), data['user_id'])
        )
            self.store()
            return data

            # Fetch all sales
            def get_all_sales(self):
            """Fetch all sales."""
            self.cursor.execute("SELECT * FROM sales")
            result=self.cursor.fetchall()
            return result

            # Fetch a sale order
            def get_a_sale_order(self, id):
            """Fetch a sale order by id."""
            self.cursor.execute(
        """
            SELECT * FROM sales WHERE sale_id='%s'
            """
        % (id)
        )
            sale=self.cursor.fetchone()
            return sale
