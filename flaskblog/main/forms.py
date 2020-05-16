from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateTimeField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class UsersForm(FlaskForm):
    user1 = StringField('User1', validators=[DataRequired()])
    user2 = StringField('User2', validators=[DataRequired()])
    submit = SubmitField('Begin Search')
