from flask import Flask, render_template, redirect, url_for
from register_form import *

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'secret_key'


def main():
    app.run()


@app.route('/')
def index():
    return redirect(url_for('feed'))


@app.route('/feed')
def feed():
    return render_template('feed.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template('feed.html')
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    main()
