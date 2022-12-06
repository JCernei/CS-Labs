from src.services.hash import hash


class UserManagementService:
    def __init__(self):
        self.database = {}

    def create_user(self, username, password):
        if username in self.database:
            print('Username already exists')
            return
        self.database[username] = hash(password)

    def validate_user(self, username_input, password_input):
        if username_input in self.database:
            if self.database[username_input] == hash(password_input):
                return True
        return False


if __name__ == "__main__":
    user_manager = UserManagementService()

    user_manager.create_user(
        username='70m_470', password='5up3r_s3cRe7_p422w0rd')

    valid_user = user_manager.validate_user(
        username_input='Tom_Ato', password_input='Super_secret_password')

    if valid_user:
        print('Great succes')
    else:
        print('Wrong Username or Password')
