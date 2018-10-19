from api import app_create

app = app_create("development")

if __name__ == "__main__":
    app.run()
