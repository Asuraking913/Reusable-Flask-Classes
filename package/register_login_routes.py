from package.UserAuth import UserAuth
from flask import request, redirect, render_template, jsonify, make_response
from package.setup.models import User

def root_routes(app):
    Auth = UserAuth()


    @app.route("/")
    def home():
        return render_template('index.html')
    
    @app.route("/api/register", methods = ['POST'])
    def handle_registration():
        if request.method == "POST":
            data = request.json
            
            response =  jsonify(Auth.create_user(data, User))
            return response
        
        return {
            'status' : 'unsucessfull', 
            'message' : 'Invalid Request'
        }, 400
    
    @app.route("/api/login", methods=['POST'])
    def handle_login():
        if request.method == "POST":
            data = request.json
            response = make_response(jsonify(Auth.login_user(data, User)))
            return response

    
    

