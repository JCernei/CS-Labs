from flask import Flask, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pyotp
import joblib
from src.cyphers.classical_cyphers.caesar import Caesar
from src.cyphers.classical_cyphers.caesar_with_keyword import CaesarWithKeyword
from src.cyphers.classical_cyphers.polybius_with_keyword import PolybiusWithKeyword
from src.cyphers.classical_cyphers.vigenere import Vigenere
from src.cyphers.symetrical_cyphers.stream.lfsr_str import LfsrStr
from src.cyphers.symetrical_cyphers.block.des import Des
from src.cyphers.asymmetrical_cyphers.rsa import Rsa

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
            return 'Usernaem already exists, go to login page'
        else:
            user = User(form_user, form_pass)
            database[form_user] = user
            return f'Use this code: {user.otp_seed} in your authenticator app'
    return 'this is the registration page'


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
        return "Invalid username, password or code. Please try again."

    return 'this is the login page'


@app.route('/logout')
def logout():
    if not session.get('username'):
        return 'visit login page first'
    session.pop('username')
    return 'you have succesfuly logout'


@app.route("/caesar", methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        text = request.form.get("text")
        key = int(request.form.get("key"))
        action = request.form.get("action")
        cypher = Caesar(key)
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using Caesar cypher'


@app.route("/caesar_with_keyword", methods=['GET', 'POST'])
def caesar_with_keyword():
    if request.method == 'POST':
        text = request.form.get("text")
        key = int(request.form.get("key"))
        keyword = request.form.get("keyword")
        action = request.form.get("action")
        cypher = CaesarWithKeyword(key, keyword)
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using Caesar cypher with keyword'


@app.route("/polybius", methods=['GET', 'POST'])
def polybius():
    if request.method == 'POST':
        text = request.form.get("text")
        keyword = request.form.get("keyword")
        action = request.form.get("action")
        cypher = PolybiusWithKeyword(keyword)
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using Polybius cypher with keyword'


@app.route("/vigenere", methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        text = request.form.get("text")
        keyword = request.form.get("keyword")
        action = request.form.get("action")
        cypher = Vigenere(keyword)
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using Vigenere cypher'


@app.route("/lfsr", methods=['GET', 'POST'])
def lfsr():
    if request.method == 'POST':
        register = request.form.get("register")
        taps = request.form.get("taps")
        text = request.form.get("text")
        action = request.form.get("action")
        cypher = LfsrStr(register, taps)
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using LFSR cypher'


@app.route("/des", methods=['GET', 'POST'])
def des():
    if request.method == 'POST':
        text = request.form.get("text")
        key = request.form.get("key")
        action = request.form.get("action")
        cypher = Des(key)
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using Des cypher'


@app.route("/rsa", methods=['GET', 'POST'])
def rsa():
    if request.method == 'POST':
        text = request.form.get("text")
        p = request.form.get("p")
        q = request.form.get("q")
        action = request.form.get("action")
        cypher = Rsa(int(p), int(q))
        if action == 'encrypt':
            return cypher.encrypt(text)
        if action == 'decrypt':
            return cypher.decrypt(text)
    return 'This is a tool that performs encryption and decryption using RSA cypher'


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
