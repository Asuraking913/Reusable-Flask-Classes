from package.UserAuth import UserAuth
from flask import request, redirect, render_template, jsonify, make_response
from package.setup.models import User
from flask_jwt_extended import create_access_token

def root_routes(app):
    Auth = UserAuth()


    @app.route("/")
    def home():
        return "<h1>This is the home page<h1>"
    
    @app.route("/api/register", methods = ['POST'])
    def handle_registration():
        if request.method == "POST":
            data = request.json
            
            response =  jsonify(Auth.create_user(data, User))
            return response
    
    

