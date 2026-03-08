from flask import Flask, request, render_template, redirect, session, flash, session as flask_session
from flask_scss import Scss
from dotenv import load_dotenv
from models import db, User, Posts, StudySession
from forms import CreateSessionForm, JoinSessionForm, DeleteSessionForm
import os
from subjects import SUBJECTS

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
    create_form = CreateSessionForm()
    joined = flask_session.get('joined', [])
    # if form.validate_on_submit():
    #     return redirect(f"/join_session/{}")
    subject_filter = request.args.get("subject")
    sessions = StudySession.query.filter_by(subject=subject_filter).all() if subject_filter else StudySession.query.all()
    return render_template("index.html", sessions=sessions, join_form=join_form, delete_form=delete_form, create_form=create_form, joined=joined, subjects=SUBJECTS, selected=subject_filter)


@app.route("/join_session/<int:id>", methods=["POST", "GET"])
def join_session(id):
    study_session = StudySession.query.get(id)

    if not study_session:
        return "Session not found", 404
    
    if 'joined' not in flask_session:
        flask_session['joined'] = []
    
    if study_session.request_only:
        flash("Request sent.")

    elif study_session.participants < study_session.capacity:
        study_session.participants += 1
    
    elif study_session.participants >= study_session.capacity:
        flash("Session capacity filled.")

    flask_session['joined'] = flask_session['joined'] + [id]
    db.session.commit()
    
    return redirect("/")

 
@app.route("/create_session", methods=["POST", "GET"])
def create_session():
    form = CreateSessionForm()
    if form.validate_on_submit():
        title = form.title.data
        subject = form.subject.data
        location = form.location.data
        capacity = form.capacity.data
        req_only = form.request_only.data
        time = form.time.data
        new_session = StudySession(title=title, subject=subject,location=location,capacity = int(capacity) if capacity else 10,request_only=req_only, time=time)
        try:
            db.session.add(new_session)
            db.session.commit()
            flash("Study session created successfully!")
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while saving.")
            print(f"Error: {e}")
    return redirect("/")

@app.route("/delete_session/<int:id>", methods=["POST"])
def delete_session(id):
    session = StudySession.query.get(id)
    if session:
        db.session.delete(session)
        db.session.commit()
        flash("Session deleted.")
    return redirect("/")


    

if __name__ in "__main__":
    with app.app_context():
        db.create_all()

        

    app.run(debug=True)
