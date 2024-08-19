from flask_bcrypt import Bcrypt
from models import User

class UserAuth:

    hasher = Bcrypt()

    def create_user(self, app, useremail, password, username = None):

        """
            By Default the username parameter is equal to None, When set to a value the database stores that value as the value of the user instance
        """
        hasher = Bcrypt(app)

        new_password = hasher.generate_password_hash(password)
        if username != None:
            new_user = User(user_name = username, user_email = useremail, user_password = new_password)
            new_user.save()

        else:
            new_user = User(user_email = useremail, user_password = new_password)
            new_user.save()
