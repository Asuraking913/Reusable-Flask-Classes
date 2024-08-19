from models import User
from extensions import hasher

class UserAuth:

    def create_user(self, useremail, password, username = None, full_credentials = False):

        """
            By Default the username parameter is equal to None, When set to a value the method sets that value to the username attribute of the user instance before sotring it
        """

        new_password = hasher.generate_password_hash(password)
        if username != None:
            new_user = User(user_name = username, user_email = useremail, user_password = new_password)
            new_user.save()

        else:
            new_user = User(user_email = useremail, user_password = new_password)
            new_user.save()
