import os

from flask import render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
from flask_restful import abort
from werkzeug.utils import secure_filename

from data import db_session
from data.db_session import create_session
from data.posts import Post
from src.forms import EditProfileForm, AddPostForm, SearchPostsForm
from src.app import login_manager, app
from data.users import get_user_by_username, User

blueprint = Blueprint('views', __name__, template_folder='../templates')



@blueprint.route('/')
def index():
    return redirect(url_for('views.feed'))


@blueprint.route('/post')
def post_test():
    session = create_session()
    post = session.query(Post).first()
    return render_template('post.html', post=post)


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
                               can_edit_profile=current_user.is_authenticated,
                               user=user)
    else:
        abort(404)


@login_required
@blueprint.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    if not current_user.is_authenticated:
        return redirect('/login')
    form = EditProfileForm()
    if form.validate() and request.method == 'POST':
        session = db_session.create_session()
        user = session.query(User).get(current_user.id)
        if form.username.data and len(form.username.data) >= 3:
            user.username = form.username.data
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
        if form.avatar.data:
            print(form.avatar.data)
            file = form.avatar.data
            filename = secure_filename(file.filename)
            user.avatar_path = 'static/img/avatars/' + filename
            print(user.avatar_path)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session.commit()
        return redirect(f'/{current_user.username if not form.username.data else form.username.data}')
    return render_template('edit_profile.html', form=form)


@login_required
@blueprint.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if not current_user.is_authenticated:
        return redirect('/login')
    form = AddPostForm()
    content = form.content.data
    if request.method == 'POST' and content:
        session = db_session.create_session()
        post = Post(user=session.query(User).get(current_user.id))
        post.content = content
        # post.tags = ''
        session.add(post)
        session.commit()
    return render_template('add_post.html', form=form)


@login_required
@blueprint.route('/search', methods=['GET', 'POST'])
@blueprint.route('/search/<query>', methods=['GET', 'POST'])
def search(query=''):
    form = SearchPostsForm()
    if request.method == 'POST':
        if query:
            hash_tags = query.split('&')
            pass  # отобразить список постов с хэштэгами hash_tags
        return redirect(f'/search/{form.query.data}')
    return render_template('search.html', form=form, query=query)


@blueprint.route('/team')
def about():
    return render_template('about.html')


@blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)
