import os
import psycopg2

# local imports
from table import queries  

class Connect(object):
    """Connect class."""

    def __init__(self):
        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Create tables."""
        i = 0
        for x in queries:
            try:
                connection = psycopg2.connect(os.getenv("DATABASE_URL"))
                cursor = connection.cursor()
                cursor.execute(x)
                connection.commit()
                cursor.close()
            except Exception as e:
                print(e)

    def destroy(self):
        """Destory tables."""
        users = "DROP TABLE IF EXISTS users CASCADE"
        category = "DROP TABLE IF EXISTS category CASCADE"
        product = "DROP TABLE IF EXISTS product CASCADE"
        sales = "DROP TABLE IF EXISTS sales CASCADE"

        eliminate = [sales, category, product, users]
        for e in eliminate:
            self.cursor.execute(e)
        self.connection.commit()
        self.cursor.close()

if __name__ == '__main__':
    Connect().destroy()
    Connect().create_tables()


