import os

from api import app_create


if __name__ == "__main__":
    config = os.getenv('FLASK_APP')
    app = app_create("development")

    app.run()
