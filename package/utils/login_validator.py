def login_validator(data, user_name):
    error = []
    if user_name:
        required_fields = ['userName', 'userEmail', 'password']
        for fields in required_fields:
            if fields not in data:
                return error.append({
                    'status' : 'uncessfull',
                    'message' : f'{fields} not provided'
                })
    else:
        required_fields = ['userEmail', 'password']
        for fields in required_fields:
            if fields not in data:
                error.append({
                    'status' : 'unsuccessfull', 
                    'message' : f'{fields} not provided'
                })
    return error