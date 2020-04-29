from flask import render_template, redirect, Blueprint, request
from flask_login import login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm
from data.db_session import create_session
from data.users import User, get_user_by_username
from flask_login import current_user

auth_bp = Blueprint('auth', __name__, template_folder='../templates')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect('/feed')
    form = RegistrationForm()
    if form.validate() and request.method == 'POST':
        if get_user_by_username(form.username.data):
            return '<h1>username has already taken</h1>'
        user = User()
        user.username = form.username.data
        user.name = form.name.data
        user.surname = form.surname.data
        # user.email = form.email.data # TODO: email verification
        user.set_password(form.password.data)
        session = create_session()
        session.add(user)
        session.commit()
        if user.check_password(form.password.data) and user.is_active:
            from datetime import timedelta
            if login_user(user, remember=True, duration=timedelta(days=50)):
                return redirect('/feed')
            else:
                return '<h1>unable to log you in</h1>'
        return redirect('/feed')
    return render_template('registration.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/feed')
    form = LoginForm()
    if form.validate() and request.method == 'POST':
        user = get_user_by_username(form.username.data)
        if not user:
            return "<h1>This user doesn't exist</h1>"
        remember_me = form.remember_me.data
        if user.check_password(form.password.data) and user.is_active:
            from datetime import timedelta
            if login_user(user, remember=remember_me, duration=timedelta(days=1)):
                return redirect('/feed')
            else:
                return '<h1>unable to log you in</h1>'
    return render_template('login.html', form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/feed')


