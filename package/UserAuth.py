from package.setup.extensions import hasher
from package.utils.validator import validator

class UserAuth:

    def create_user(self, data, User, username = False, full_credentials = False):

        """ 
        User:
            Takes ther User Model as an argument and query's it for existing emails address, returns a 400 https response/status code 
            if such email address is found


        By default the user_name argument is set to False causing the username not to be taken into account during validation Except if set to true

        By default the full_credentials argument is set to false, when set to true, Validation for other entries like
        firsName and lastname becomes available

        Valid fields should comes as...

        For Default Validation
            userEmail
            password1 
            password2
        
        For Validation with userName

            userName
            userEmail
            password1 
            password2
            
        For full credentials
            firstName
            lastName
            password1
            password2
            phone
        """
        
        error = validator(data, User, user_name = username, full_credentials=full_credentials) #handles Validation and returns appropriate http response code for invalid fields
        print(error)
        if error != []:
            return {
            'status' : 'unsucessfull', 
            'error' : error 
            }, 400
        
        new_password = hasher.generate_password_hash(data['password1'])
        if username:
            new_user = User(user_name = data['userName'], user_email = data['userEmail'], user_password = new_password)
            try:
                new_user.save()
            except Exception as e:
                new_user.rollback()
            return {
                'status' : 'successfull', 
                'message' : 'Created new_user'
            }, 201

        if full_credentials:
            new_user = User(user_email = data['userEmail'], user_password = new_password, first_name = data['firstName'], last_name = data['lastName'], phone = data['phone'])
            return {
                'status' : 'successfull', 
                'message' : 'Created new_user'
            }, 201

        #default setting
        new_user = User(user_email = data['userEmail'], user_password=new_password)
        new_user.save()
        return {
        'status' : 'successfull', 
        'message' : 'Created new_user'
        }, 201