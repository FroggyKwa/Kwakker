from flask import Flask, render_template, redirect, url_for
from flask_restful import reqparse, abort, Api, Resource
from src import create_app
from auth import *
from data import db_session
from api import add_resources

app = create_app()
app.config['SECRET_KEY'] = 'secret_key'
api = Api(app)
api = add_resources(api)
db_session.global_init("../db/database.sqlite")


def main():
    app.run()


@app.route('/')
def index():
    return redirect(url_for('feed'))


@app.route('/feed')
def feed():
    return render_template('feed.html')


if __name__ == '__main__':
    main()
