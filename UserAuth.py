from models import User
from extensions import hasher
import random

class UserAuth:

    def create_user(self, data, username = False, full_credentials = False):

        """
            By Default the username parameter is equal to None, When set to a value the method sets that value to the username attribute of the user instance before sotring it
        """

        new_password = hasher.generate_password_hash(data['password1'])
        if username:
            new_user = User(user_name = data['userName'], user_email = data['userEmail'], user_password = new_password)
            new_user.save()
        
        if full_credentials:
            new_user = User(user_email = data['userEmail'], user_password = new_password, first_name = data['firstName'], last_name = data['lastName'], phone = data['phone'])

        
        new_user = User(user_name = data['userName'], user_email = data['userEmail'], user_password=new_password)
        new_user.save()
