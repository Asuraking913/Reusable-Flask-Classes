from UserAuth import UserAuth
from flask import request, redirect, render_template
from models import User

def root_routes(app):
    Auth = UserAuth()


    @app.route("/")
    def home():
        return "<h1>This is the home page<h1>"
    
    @app.route("/api/register", methods = ['POST'])
    def handle_registration():
        if request.method == "POST":
            data = request.json
            
            response = Auth.create_user(data, User)
            return response

