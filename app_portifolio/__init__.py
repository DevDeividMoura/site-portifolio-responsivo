import os, sys
sys.path.append("..")
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

# Load the config file
if os.getenv("FLASK_ENV") == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print(app.config.get("MAIL_USERNAME"))
mail = Mail(app)

from app_portifolio import routes
