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
    sessions = StudySession.query.all()
    join_form = JoinSessionForm()
    delete_form = DeleteSessionForm()
    # if form.validate_on_submit():
    #     return redirect(f"/join_session/{}")
    return render_template("index.html", sessions=sessions, join_form=join_form, delete_form=delete_form)


@app.route("/join_session/<int:id>", methods=["POST", "GET"])
def join_session(id):
    session = StudySession.query.get(id)

    if not session:
        return "Session not found", 404
    
    if session.request_only:
        flash("Request sent.")

    elif session.participants < session.capacity:
        session.participants += 1
    
    elif session.participants >= session.capacity:
        flash("Session capacity filled.")
    db.session.commit()
    
    return redirect("/")

 
@app.route("/create_session", methods=["POST", "GET"])
def create_session():
    # form = CreateSessionForm()
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
        return redirect("/")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while saving.")
        print(f"Error: {e}")
    # return render_template("create_session.html", form=form)

    

if __name__ in "__main__":
    with app.app_context():
        db.create_all()

        

    app.run(debug=True)
