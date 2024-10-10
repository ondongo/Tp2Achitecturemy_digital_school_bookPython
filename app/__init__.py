from flask import Flask
from flask_restx import Api
from app.models import db
from config import Config
from app.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialisation de la base de données
    db.init_app(app)

    # Initialisation de l'API Flask-RESTx
    api = Api(app)

    # Enregistrement des namespaces
    register_routes(api)

    with app.app_context():
        db.create_all()

    return app
