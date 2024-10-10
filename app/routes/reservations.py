from flask_restx import Resource, Namespace
from app.services import BibliothequeService

api = Namespace("reservations", description="Opérations de réservation")
service = BibliothequeService()


@api.route("/<int:livre_id>/<int:utilisateur_id>")
class Reservation(Resource):
    def post(self, livre_id, utilisateur_id):
        """Réserver un livre"""
        result = service.reserver_livre(livre_id, utilisateur_id)
        return {"message": result}, 201


@api.route("/annuler/<int:reservation_id>")
class AnnulationReservation(Resource):
    def delete(self, reservation_id):
        """Annuler une réservation"""
        result = service.annuler_reservation(reservation_id)
        return {"message": result}, 200
