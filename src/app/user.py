from werkzeug.security import generate_password_hash
import pyotp


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.otp_seed = pyotp.random_base32()
        self.role = 'user'
        if username == 'admin':
            self.role = 'admin'
