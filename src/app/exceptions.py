from werkzeug.exceptions import Unauthorized


class NotLoggedIn(Exception):
    pass


def check_login_status(session):
    if not session.get('username'):
        raise NotLoggedIn()


def validate_admin(user):
    if user.role != 'admin':
        raise Unauthorized
    pass


class InvalidAuthentication(Exception):
    pass
