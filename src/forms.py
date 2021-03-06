from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, \
    FileField
from wtforms.validators import DataRequired, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname')
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Rembember me')
    submit = SubmitField('Sign in')


class EditProfileForm(FlaskForm):
    username = StringField('Login')
    name = StringField('Name')
    surname = StringField('Surname')
    age = IntegerField('Age')
    status = TextAreaField('Status')
    password = PasswordField('Password')
    avatar = FileField('File Upload')
    submit = SubmitField('Save')


class AddPostForm(FlaskForm):
    content = TextAreaField('Content')
    submit = SubmitField('Add Post')


class SearchPostsForm(FlaskForm):
    query = StringField('Query')
    submit = SubmitField('Search')
