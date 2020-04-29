from flask import render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
from flask_restful import abort

from data import db_session
from data.db_session import create_session
from forms import EditProfileForm
from app import login_manager
from data.users import get_user_by_username, User

blueprint = Blueprint('views', __name__, template_folder='../templates')


@blueprint.route('/post')
def post():
    return render_template('post.html',
                           db_id=1,
                           author='denchik',
                           created_at='20.04.2020',
                           content='Lorem ipsum dolor sit amet, '
                                   'consectetur adipiscing elit, sed do'
                                   ' eiusmod tempor incididunt ut labore et'
                                   ' dolore magna aliqua. Ut enim ad',
                           likes=1337,
                           tags=['#web', '#cool'])


@blueprint.route('/')
def index():
    return redirect(url_for('views.feed'))


@login_required
@blueprint.route('/feed')
def feed():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('feed.html')


@blueprint.route('/<username>')
def profile(username):
    user = get_user_by_username(username)
    if user:
        return render_template('profile.html',
                               image=f'{current_user.username}.gif',
                               can_edit_profile=True,
                               user=user)
    else:
        abort(404)


@login_required
@blueprint.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    if not current_user.is_authenticated:
        return redirect('auth.login')
    form = EditProfileForm()
    if form.validate() and request.method == 'POST':
        print('hello')
        session = db_session.create_session()
        user = session.query(User).get(current_user.id)
        if form.username.data and len(form.username.data) >= 3:
            user.username = form.username.data
            print('hello, world')
        if form.password.data and len(form.password.data) >= 6:
            user.password = form.password.data
        if form.surname.data:
            user.surname = form.surname.data
        if form.name.data:
            user.name = form.name.data
        if form.age.data:
            user.age = form.age.data
        if form.status.data:
            user.status = form.status.data
        session.commit()

    return render_template('edit_profile.html', form=form)


@blueprint.route('/post')
def post():
    return render_template('post.html')


@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)
