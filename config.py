import os


class ProductionConfig:  # pylint: disable=R0903
    """PROD"""

    # FLASK
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "Ch@nG3_ME!")

    # # DATABASE
    # SQLALCHEMY_BINDS = {
    #     'radius': os.getenv("DATABASE_URI") + '/radius',
    #     'app': os.getenv("DATABASE_URI") + '/app' 
    # }
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # # AUTH and JWT
    # JWT_ISS = os.getenv("JWT_ISS", "https://confrarianews.com.br")


class DevelopmentConfig(ProductionConfig):  # pylint: disable=R0903
    """DEV"""

    FLASK_ENV = "development"
    DEBUG = True
