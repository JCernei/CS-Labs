from flask import Flask, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pyotp
import joblib

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(16).hex()
database = {}


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.otp_seed = pyotp.random_base32()


@app.route("/")
def index():
    if not session.get('username'):
        return 'visit login page first'

    return 'congratulations you passed the 2FA'


@app.route("/register", methods=['GET', 'POST'])
def register():
    form_user = request.form.get("username")
    form_pass = request.form.get("password")
    if request.method == 'POST':
        if form_user in database:
            return 'Usernaem already exists, go to login'
        else:
            user = User(form_user, form_pass)
            database[form_user] = user
            return f'Use this code: {user.otp_seed} in your authenticator app'
    return 'this is registration page'


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_user = request.form.get("username")
    form_pass = request.form.get("password")

    totp_instance = pyotp.TOTP(database[form_user].otp_seed)
    valid = totp_instance.verify(request.form.get("otp"))

    if request.method == 'POST':
        if valid and form_user in database and check_password_hash(database[form_user].password_hash, form_pass):
            session['username'] = form_user
            return 'you can go to index page now'
        return ("Invalid username, password or code. Please try again.")

    return 'this is log in page'


@app.route('/logout')
def logout():
    if not session.get('username'):
        return 'visit login page first'
    session.pop('username')
    return 'you have succesfuly logout'


@app.teardown_appcontext
def on_exit(ctx):
    joblib.dump(database, 'db.save')


if __name__ == "__main__":
    try:
        database = joblib.load('db.save')
        print(database.keys())
    except:
        pass

    app.run(debug=True)
