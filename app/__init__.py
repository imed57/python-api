from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    jwt = JWTManager(app)

    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app
