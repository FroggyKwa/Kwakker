def create_app():
    from flask import Flask, render_template, redirect, url_for
    from auth import bp

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = 'secret_key'
    app.register_blueprint(bp)
    return app

