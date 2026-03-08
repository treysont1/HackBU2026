@app.route("/join_session/<int:id>", methods=["GET"])
def join_session(id):
    session = StudySession.query.get(id)

    if session.request_only:
        flash("Request sent.")

    elif session.participants < session.capacity:
        session.participants += 1
    
    elif session.participants >= session.capacity:
        flash("Session capacity filled.")
    
    return redirect("/")
    