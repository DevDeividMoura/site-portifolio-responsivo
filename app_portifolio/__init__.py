import os, sys
sys.path.append("..")
from flask import Flask

app = Flask(__name__)

# Load the config file
if os.getenv("FLASK_ENV") == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app_portifolio import routes
