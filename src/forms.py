from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, TextAreaField
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
    remember_me = BooleanField('Repeat password')
    submit = SubmitField('Sign in')


class EditProfileForm(FlaskForm):
    username = StringField('Login', validators=[validators.Length(max=32)])
    name = TextAreaField('Name', validators=[validators.Length(min=4, max=20)])
    surname = StringField('Surname', validators=[validators.Length(min=4, max=25)])
    status = StringField('Status', validators=[validators.Length(max=128)])
    password = PasswordField('Password', validators=[validators.Length(min=6, max=64)])
