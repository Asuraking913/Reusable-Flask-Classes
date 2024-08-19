from UserAuth import UserAuth
from flask import request, redirect, render_template
from utils.validator import validator

def root_routes(app):
    Auth = UserAuth()


    @app.route("/")
    def home():
        return "<h1>This is the home page<h1>"
    
    @app.route("/api/register", methods = ['POST'])
    def handle_registration():
        if request.method == "POST":
            data = request.json
            error = validator(data)
            if error != []:
                return {
                'status' : 'unsucessfull', 
                'error' : error 
                }
            
            username = data['user_name']

