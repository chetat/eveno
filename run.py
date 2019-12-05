from app import create_app, sqlalchemy
from app.config import DevelopmentConfig

app = create_app(config_obj=DevelopmentConfig)


if __name__=="__main__":
    app.run()