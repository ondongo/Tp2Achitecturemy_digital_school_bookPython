from app.models import db, Livre, Utilisateur, Pret, Reservation
from datetime import datetime


class BibliothequeService:
    def ajouter_livre(self, titre, auteur):
        if Livre.query.filter_by(titre=titre).first():
            return "Un livre avec ce titre existe déjà."
        nouveau_livre = Livre(titre=titre, auteur=auteur)
        db.session.add(nouveau_livre)
        db.session.commit()
        return "Livre ajouté avec succès."

    def emprunter_livre(self, livre_id, utilisateur_id):
        livre = db.session.get(Livre, livre_id)
        if not livre.disponible:
            return "Le livre est déjà emprunté."
        livre.disponible = False
        pret = Pret(livre_id=livre_id, utilisateur_id=utilisateur_id)
        db.session.add(pret)
        db.session.commit()
        return "Livre emprunté avec succès."

    def retourner_livre(self, pret_id):
        pret = Pret.query.get(pret_id)
        if not pret:
            return "Prêt introuvable."
        livre = pret.livre
        livre.disponible = True
        pret.date_retour = datetime.utcnow()
        db.session.commit()
        return "Livre retourné avec succès."

    def reserver_livre(self, livre_id, utilisateur_id):
        livre = db.session.get(Livre, livre_id)
        if not livre.disponible:
            reservation = Reservation(livre_id=livre_id, utilisateur_id=utilisateur_id)
            db.session.add(reservation)
            db.session.commit()
            return "Réservation effectuée avec succès."
        return "Le livre est disponible, pas besoin de réservation."

    def annuler_reservation(self, reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if not reservation:
            return "Réservation introuvable."
        db.session.delete(reservation)
        db.session.commit()
        return "Réservation annulée."

    def lister_livres(self):
        """Retourne la liste de tous les livres disponibles dans la bibliothèque."""
        livres = Livre.query.all()
        return livres

    def voir_detail_livre(self, livre_id):
        """Retourne les détails d'un livre spécifique."""
        livre = db.session.get(Livre, livre_id)
        if not livre:
            return None, "Livre introuvable."
        return livre, "Détails du livre récupérés avec succès."
