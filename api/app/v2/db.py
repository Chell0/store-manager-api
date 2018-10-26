import os
import psycopg2


class StoreDb:
    def __init__(self):
        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.cursor = self.connection.cursor()
        # self.connection.commit()
        # self.cursor.close()
