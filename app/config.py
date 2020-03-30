
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Signal application everytime there is a change in Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    print(SQLALCHEMY_DATABASE_URI)

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2


class DevelopmentConfig(Config):
    # Statement for enabling the development environment
    ENV = "development"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
