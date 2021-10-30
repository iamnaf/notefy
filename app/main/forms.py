from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    name = StringField("Enter Your Name", validators=[DataRequired()])
    comment = StringField("Enter Your Comment", validators=[DataRequired()])
    submit = SubmitField('Submit')

class NoteForm(FlaskForm):
    author = StringField("Note Author", validators=[DataRequired()])
    title = StringField("Note Title", validators=[DataRequired()])
    body = TextAreaField("Note Body", validators=[DataRequired()])
    submit = SubmitField("Submit")