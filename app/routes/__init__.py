from flask_restx import Api
from .livres import api as livre_api
from .emprunts import api as emprunt_api
from .reservations import api as reservation_api

def register_routes(api: Api):
    api.add_namespace(livre_api, path='/livres')
    api.add_namespace(emprunt_api, path='/emprunts')
    api.add_namespace(reservation_api, path='/reservations')
