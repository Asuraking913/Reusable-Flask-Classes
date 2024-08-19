from UserAuth import UserAuth
from flask import request, redirect, render_template
from utils.validator import validator
import random

def root_routes(app):
    Auth = UserAuth()


    @app.route("/")
    def home():
        return "<h1>This is the home page<h1>"
    
    @app.route("/api/register", methods = ['POST'])
    def handle_registration():
        if request.method == "POST":
            data = request.json
            error = validator(data, user_name=True)
            if  error:
                print('event')
                print(error)
                return {
                'status' : 'unsucessfull', 
                'error' : error 
                }, 400
            
            
            Auth.create_user(data=data, username=True)
            return {
                'status' : 'successfull', 
                'message' : 'Created new_user'
            }

