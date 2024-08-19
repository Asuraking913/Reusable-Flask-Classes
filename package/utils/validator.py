def validator(data, User, user_name = False, full_credentials=False):

    """
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
    error = []
    #full credentials False
    if full_credentials == False:
        if user_name:
            required_fields = ['userName', 'userEmail', 'password1', 'password2']

            for field in required_fields:
                if field not in data:
                    error.append({
                        'error' : f'{field} not provided'
                    })

            #checking password matching
            if 'password1' and 'password2' not in data:
                error.append({ 
                    'error' : 'Password entries do not match'
                })
                return error
            
            #Checking User model for existing emails
            if 'userEmail' in data:
                user = User.query.filter_by(user_email = data['userEmail']).first()
                print(user)
                if user != None:
                    error.append({
                        'status' : 'unsuccessfull', 
                        'message' : 'User Email Already exists'
                    })

        else:
            #Default setting
            required_fields = ['userEmail', 'password1', 'password2']
            for field in required_fields:
                if field not in data:
                    error.append({
                        'error' : f'{field} not provided'
                    })

                #Checking User model for existing emails
                if 'userEmail' in data:
                    user = User.query.filter_by(user_email = data['userEmail']).first()
                    print(user)
                    if user != None:
                        error.append({
                            'status' : 'unsuccessfull', 
                            'message' : 'User Email Already exists'
                        })
                
                #checking password matching
                if 'password1' and 'password2' not in data:
                    error.append({ 
                    'error' : 'Password entries do not match'
                })
                return error

        
    else:
        #full_credentials true
        required_fields = ['firstName', 'lastName', "userName", 'userEmail', 'password1', "password2", "phone"]
        for field in required_fields:
            if field not in data:
                error.append({
                        'error' : f'{field} not provided'
                    })
            
            #checking password matching
            if 'password1' and 'password2' not in data:
                error.append({ 
                    'error' : 'Password entries do not match'
                })
                return error
                
                #Checking User model for existing emails
            if 'userEmail' in data:
                user = User.query.filter_by(user_email = data['userEmail']).first()
                print(user)
                if user != None:
                    error.append({
                        'status' : 'unsuccessfull', 
                        'message' : 'User Email Already exists'
                    })
                return error
    
    print('event')
    print(error)
    return error
    