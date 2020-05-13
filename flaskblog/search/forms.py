from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired
from datetime import datetime


class SearchForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date', default=datetime.utcnow)
    submit = SubmitField('Post Blog')
