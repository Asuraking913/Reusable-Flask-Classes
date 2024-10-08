from package.setup.extensions import hasher
from package.utils.validator import validator
from package.utils.login_validator import login_validator
from flask_jwt_extended import create_access_token, set_access_cookies
from flask import make_response, jsonify


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
    
    def login_user(self, data, User, cookies = False, username = False):

        '''
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
        
        The cookies argument by default is set to False...
        this causes the jwt token to be included in the response...
        When set to true the response does not return the token insteads includes it the cookie...

        A JWT_CSRF_TOKEN token is sent to the cookies too, setting JWT_CSRF_IN_COOKIES to False disables this cookies
        from subsequent request
        '''

        error = login_validator(data, user_name=username)

        if error != []:
            return {
                'status' : 'unsuccessfull',
                'error' : error
            }, 400

        current_user = User.query.filter_by(user_email = data['userEmail']).first()
        if current_user != None:
            if hasher.check_password_hash(current_user.user_password, data['password']):
                access_token = create_access_token(current_user._id)
                if not cookies:
                    response =  make_response(jsonify({
                        'status' : 'sucessfull', 
                        'message' : 'User Logged in sucessfully', 
                        "data" : {
                            'access_token' : access_token,
                            'userId' : current_user._id,
                            'userName' : current_user.user_name, 
                            'firstName' : current_user.first_name, 
                            'lastName' : current_user.last_name, 
                            'phone' : current_user.phone
                        } 
                    }))

                    return response, 200
            
                response =  make_response(jsonify({
                        'status' : 'sucessfull', 
                        'message' : 'User Logged in sucessfully', 
                        "data" : {
                            'userId' : current_user._id,
                            'userName' : current_user.user_name, 
                            'firstName' : current_user.first_name, 
                            'lastName' : current_user.last_name, 
                            'phone' : current_user.phone
                        } 
                    }))


                set_access_cookies(response, access_token)
                return response, 200
            
            return {
                    'status' : 'unsucessfull', 
                    'message' : 'Incorrect password'
                }, 400
        
        return {
                    'status' : 'unsucessfull', 
                    'message' : 'Invalid username/email'
                }, 400


            


            