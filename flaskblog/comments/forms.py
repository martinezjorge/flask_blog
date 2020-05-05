from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    sentiment = SelectField('Sentiment',
                            choices=[('Positive', 'Positive'), ('Negative', 'Negative')],
                            validators=[DataRequired()])
    submit = SubmitField('Post Comment')
