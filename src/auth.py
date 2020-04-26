import requests
from flask import render_template, redirect, url_for, Blueprint, request, session
from flask_login import login_user, logout_user, login_required
from flask_restful import abort
from passlib.hash import sha256_crypt
from app import login_manager
from forms import RegistrationForm, LoginForm
from data.db_session import create_session
from data.users import User, get_user_by_username
from flask_login import current_user

bp = Blueprint('auth', __name__, template_folder='../templates')


@bp.route('/signup', methods=['GET', 'POST'])
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
        # user.password = str(sha256_crypt.encrypt((str(form.password.data))))  # TODO: DON'T SAVE TO DB
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


@bp.route('/login', methods=['GET', 'POST'])
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


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/feed')


@bp.route('/')
def index():
    return redirect(url_for('auth.feed'))


@bp.route('/feed')
def feed():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('feed.html')


@bp.route('/<username>')
def profile(username):
    if get_user_by_username(username):
        return render_template('profile.html', image=f'{current_user.username}.gif')
    else:
        abort(404)

# @bp.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404 TODO: MAKE THE 404 PAGE


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)
