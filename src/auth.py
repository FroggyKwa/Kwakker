from flask import render_template, redirect, url_for, Blueprint, request, session
from passlib.hash import sha256_crypt
from forms import RegistrationForm
from data.db_session import create_session
from data.users import User
import requests

bp = Blueprint('auth', __name__, template_folder='../templates')


@bp.route('/register', methods=['GET', 'POST'])
@bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate() and request.method == 'POST':
        user = User()
        user.username = form.username.data
        print(requests.get(f'http://localhost:5000/api/v01/user/{user.username}').json())
        if 'error' not in requests.get(f'http://localhost:5000/api/v01/user/{user.username}').json():
            return 'username has already taken'
        user.name = form.name.data
        user.surname = form.surname.data
        # user.email = form.email.data # TODO: email verification
        user.password = str(sha256_crypt.encrypt((str(form.password.data))))
        session = create_session()
        session.add(user)
        session.commit()
        return redirect('/feed')
    return render_template('registration.html', form=form)
