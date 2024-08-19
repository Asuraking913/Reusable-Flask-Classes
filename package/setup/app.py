from flask import Flask
from package.setup.extensions import hasher, jwt, db
from package.setup.config import Appconfig
from package.register_login_routes import root_routes

def create_app():

    app = Flask(__name__)
    app.config.from_object(Appconfig)

    jwt.init_app(app)
    hasher.init_app(app)
    root_routes(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
