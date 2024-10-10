from database import db
from datetime import datetime


class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    disponible = db.Column(db.Boolean, default=True)

class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

class Pret(db.Model):
    __tablename__ = 'prets'
    id = db.Column(db.Integer, primary_key=True)
    livre_id = db.Column(db.Integer, db.ForeignKey('livres.id'), nullable=False)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'), nullable=False)
    date_pret = db.Column(db.DateTime, default=datetime.utcnow)
    date_retour = db.Column(db.DateTime, nullable=True)

    livre = db.relationship('Livre', backref='prets')
    utilisateur = db.relationship('Utilisateur', backref='prets')

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    livre_id = db.Column(db.Integer, db.ForeignKey('livres.id'), nullable=False)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'), nullable=False)
    date_reservation = db.Column(db.DateTime, default=datetime.utcnow)

    livre = db.relationship('Livre', backref='reservations')
    utilisateur = db.relationship('Utilisateur', backref='reservations')
