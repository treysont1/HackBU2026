from flask import Flask, request, render_template, redirect, session, flash
from flask_scss import Scss
from dotenv import load_dotenv
from models import db, User, Posts, StudySession
from forms import CreateSessionForm, JoinSessionForm, DeleteSessionForm
import os

app = Flask(__name__)

load_dotenv(dotenv_path=".env")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.secret_key = os.getenv("SECRET_KEY")

db.init_app(app)
Scss(app)



@app.route("/")
def index():
    return render_template("index.html")



if __name__ in "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)