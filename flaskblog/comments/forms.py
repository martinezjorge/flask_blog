from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    content = StringField('Tags', validators=[DataRequired()])
    sentiment = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Blog')
