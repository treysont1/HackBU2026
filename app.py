from flask import Flask, request
from flask_scss import Scss
from models import db
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.secret_key = os.getenv("SECRET_KEY")

db.init_app(app)
Scss(app)



@app.route("/")
def index():
    return "hi"



if __name__ in "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)