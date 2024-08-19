from flask import Flask
from extensions import jwt, db
from config import Appconfig
from routes import root_routes
from extensions import hasher

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
