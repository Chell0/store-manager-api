import os

from api import app_create

config = os.getenv('APP_SETTINGS')  # development cofiguration
app = app_create(config)

if __name__ == '__main__':
    app.run()
