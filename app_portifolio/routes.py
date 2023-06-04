from flask import render_template, redirect
from app_portifolio import app

@app.route("/")
def index():
    return render_template("index.html")