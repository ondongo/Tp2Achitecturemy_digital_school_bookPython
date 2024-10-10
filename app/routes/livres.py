from flask_restx import Resource, Namespace, fields
from flask import request
from app.services import BibliothequeService

api = Namespace("livres", description="Opérations sur les livres")
service = BibliothequeService()

livre_model = api.model(
    "Livre",
    {
        "titre": fields.String(required=True, description="Titre du livre"),
        "auteur": fields.String(required=True, description="Auteur du livre"),
    },
)


@api.route("/")
class LivreList(Resource):
    @api.marshal_list_with(livre_model)
    def get(self):
        """Lister tous les livres"""
        return service.lister_livres()

    @api.expect(livre_model)
    def post(self):
        """Ajouter un nouveau livre"""
        data = request.get_json()
        result = service.ajouter_livre(data["titre"], data["auteur"])
        return {"message": result}, 201


@api.route("/<int:livre_id>")
class LivreDetail(Resource):
    @api.marshal_with(livre_model)
    def get(self, livre_id):
        """Voir les détails d'un livre"""
        livre, message = service.voir_detail_livre(livre_id)
        if livre:
            return livre
        api.abort(404, message)
