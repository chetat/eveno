from app import create_app, sqlalchemy
from app.config import Config

app = create_app(Config)


if __name__ == "__main__":
    app.run()
