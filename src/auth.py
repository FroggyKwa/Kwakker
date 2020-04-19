from flask import render_template, redirect, url_for, Blueprint, request
from passlib.hash import sha256_crypt
from forms import RegistrationForm
from data.db_session import create_session
from data.users import User

bp = Blueprint('auth', __name__, template_folder='../templates')


@bp.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate() and request.method == 'POST':
        user = User()
        user.username = form.username.data
        user.name = form.name.data
        user.surname = form.surname.data  # TODO: ADD to api ?
        user.email = form.email.data
        user.password = sha256_crypt.encrypt((str(form.password.data)))
        session = create_session()
        session.add(user)
        session.commit()
        return redirect('/feed')
    return render_template('registration.html', form=form)
