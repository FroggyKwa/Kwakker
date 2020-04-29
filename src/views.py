from flask import render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
from flask_restful import abort

from data.db_session import create_session
from forms import EditProfileForm
from app import login_manager
from data.users import get_user_by_username, User

blueprint = Blueprint('views', __name__, template_folder='../templates')


@blueprint.route('/')
def index():
    return redirect(url_for('views.feed'))


@login_required
@blueprint.route('/feed')
def feed():
    if not current_user.is_authenticated:
        return redirect(url_for('views.login'))
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


@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)
