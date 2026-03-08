"""
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
"""
"""
@app.route("/join_session/<int:id>", methods=["GET"])
def join_session():
    session = StudySession.query.get(id)

    if session.request_only:
        flash("Request sent.")

    elif session.participants < session.capacity:
        session.participants += 1
    
    elif session.participants >= session.capacity:
        flash("Session capacity filled.")
    
    return redirect("/")

 
@app.route("/create_session", methods=["POST"])
def create_session():
    title = request.form.get("title")
    subject = request.form.get("subject")
    location = request.form.get("location")
    capacity = request.form.get("capacity") 
    req_only = request.form.get("request_only") == "on"
    new_session = StudySession(title=title, subject=subject,location=location,capacity = int(capacity) if capacity else 10,request_only=req_only)
    try:
        db.session.add(new_session)
        db.session.commit()
        flash("Study session created successfully!")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while saving.")
        print(f"Error: {e}")

    return redirect("/")


@app.route("/get_session", methods=["GET"])
def get_session():
    return f'<h3>{ StudySession.query.get(1).title}'
"""
"""
@app.route("/create_session", methods=["POST"])
def create_session():
    print(request.form)
    title1 = request.form.get("title")
    subject1 = request.form.get("subject")
    location1 = request.form.get("location")
    req_only = request.form.get("req_only")
    first = StudySession(title = title1, subject = subject1, location = location1, request_only = req_only)
    db.session.add(first)
    db.session.commit()
    return redirect("/")

@app.route("/get_session", methods=["GET"])
def get_session():
    return f'<p>{StudySession().query.get(1)}</p> <p>{StudySession().query.get(1)}</p> <p>{StudySession().query.get(1)}</p>'
"""


"""
@app.route("/temp_session", methods = ["POST"])
def temp_session_post():
    data = request.form.get("word")     
    print(data)
    return f'<p>{data}</p>'
@app.route("/temp_session", methods = ["GET"])
def temp_session_get():
    return f'<p>n</p>'

if __name__ in "__main__":
    with app.app_context():
        db.create_all()

        

    app.run(debug=True)
"""