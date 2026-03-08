from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, DateTimeLocalField, IntegerField, HiddenField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError
from subjects import subject_choices


class CreateSessionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subject = SelectField('Subject', choices=subject_choices, validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    time = DateTimeLocalField('Date')
    description = StringField('Short Description', validators=[DataRequired()])
    capacity = IntegerField("Limit of People")
    request_only = BooleanField('Request Only')
    submit = SubmitField('Create')

class JoinSessionForm(FlaskForm):
    session_id = HiddenField()
    submit = SubmitField()

class DeleteSessionForm(FlaskForm):
    session_id = HiddenField()
    submit = SubmitField("Delete")

#HELLO

