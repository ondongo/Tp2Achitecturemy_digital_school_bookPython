import unittest
from app import create_app, db
from app.models import Livre, Utilisateur

class TestEmprunts(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()
        self.utilisateur = Utilisateur(nom="Test User", email="testuser@example.com")
        self.livre = Livre(titre="Test Livre", auteur="Auteur Test")
        db.session.add(self.utilisateur)
        db.session.add(self.livre)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_emprunter_livre(self):
        response = self.client.post(f'/emprunts/{self.livre.id}/{self.utilisateur.id}')
        self.assertEqual(response.status_code, 201)
        """ self.assertIn('Livre emprunté avec succès', response.data.decode('utf-8'))  """