from flask_restx import Resource, Namespace
from app.services import BibliothequeService

api = Namespace('emprunts', description='Opérations d\'emprunt')
service = BibliothequeService()

@api.route('/<int:livre_id>/<int:utilisateur_id>')
class Emprunt(Resource):
    def post(self, livre_id, utilisateur_id):
        '''Emprunter un livre'''
        result = service.emprunter_livre(livre_id, utilisateur_id)
        return {'message': result}, 201

@api.route('/retour/<int:pret_id>')
class Retour(Resource):
    def post(self, pret_id):
        '''Retourner un livre'''
        result = service.retourner_livre(pret_id)
        return {'message': result}, 200
