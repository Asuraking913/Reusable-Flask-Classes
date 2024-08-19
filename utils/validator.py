def validator(data, user_name = False, full_credentials=False):

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
            FirstName
            LastName
            password1
            password2
            phone


    """
    error = []
    if full_credentials == False:
        if user_name != None:
            required_fields = ['userName', 'userEmail', 'password1', 'password2']

            for field in required_fields:
                if field not in data:
                    error.append({
                        'error' : f'{field} not provided'
                    })
            if 'password1' and 'password2' not in data:
                error.append({ 
                    'error' : 'Password entries do not match'
                })
                return error

        else:
            required_fields = ['userEmail', 'password1', 'password2']
            for field in required_fields:
                if field not in data:
                    error.append({
                        'error' : f'{field} not provided'
                    })
                return error
        
    else:
        required_fields = ['firstName', 'lastName', "userName" 'userEmail', 'password1', "password2", "phone"]
        for field in required_fields:
            if field not in data:
                error.append({
                        'error' : f'{field} not provided'
                    })
                return error
        
    