# BiblioMydigitalSchool

BiblioMydigitalSchool est une application de gestion de bibliothèque développée en Python avec Flask, utilisant une architecture à trois couches et une base de données SQLite. Elle permet d'ajouter, emprunter, retourner et réserver des livres, le tout via une API REST.

## Fonctionnalités

- **Ajout de livre** : Ajouter des livres à la bibliothèque.
- **Emprunt de livre** : Emprunter des livres si disponibles.
- **Retour de livre** : Retourner un livre emprunté.
- **Réservation de livre** : Réserver un livre non disponible.
- **Lister les livres** : Voir tous les livres disponibles dans la bibliothèque.
- **Voir les détails d'un livre** : Voir les détails d'un livre spécifique.

## Technologies utilisées

- Python 3.x
- Flask
- Flask-RESTx
- SQLite
- SQLAlchemy

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- `pip`, le gestionnaire de paquets Python

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/biblio-app.git
   cd biblio-app
   ```
2. Créez un environnement virtuel (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Pour Linux/MacOS
   venv\Scripts\activate  # Pour Windows
   ```
3. Installez les dépendances du projet :

   ```bash
   pip install -r requirements.txt
   ```
4. Configurez l'application :

   - Les configurations se trouvent dans le fichier `config.py`.
   - La base de données sera automatiquement créée lors du premier lancement.

## Démarrer l'application

1. Pour démarrer le serveur Flask :

   ```bash
   python run.py
   ```
2. L'application sera disponible à l'adresse suivante :

   ```
   http://127.0.0.1:5000/
   ```

## Utilisation de l'API

- **Endpoint pour lister les livres** :
  ``GET /livres``
- **Endpoint pour ajouter un livre** :
  ``POST /livres``

  - Corps de la requête :

  ```json
  {
      "titre": "Nom du Livre",
      "auteur": "Auteur du Livre"
  }
  ```

## Structure du Projet

biblio-app/
│
├── app/
│ ├── models.py # Définition des modèles SQLAlchemy (Livre, Utilisateur, Pret, Reservation)
│ ├── routes/
│ │ ├── livres.py # Endpoints pour les opérations sur les livres
│ │ └── emprunts.py # Endpoints pour emprunter/retourner les livres
│ ├── services/
│ │ ├── bibliotheque_service.py # Services métiers (ajouter, emprunter, lister, réserver)
│ └──  **init** .py # Initialisation de l'application Flask
│
├── tests/
│ ├── test_livres.py # Tests unitaires pour les fonctionnalités de livres
│ └── test_emprunts.py # Tests unitaires pour les emprunts de livres
│
├── config.py # Fichier de configuration (base de données, secret key)
├── database.py # Gestion de l'initialisation de la base de données
├── requirements.txt # Dépendances Python
├── run.py # Script pour démarrer l'application Flask
└── README.md # Documentation du projet

## Lancer les tests

Les tests valident les fonctionnalités principales de l'application, telles que l'ajout de livres, l'emprunt et la réservation.

    Les tests unitaires sont situés dans le répertoire`tests/`.

    Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
pytest
```

    Pour exécuter tous les tests à la fois, vous pouvez utiliser la commande suivante :

```bash
python -m unittest discover -s tests
```

### Exemple de test unitaire pour les livres (fichier : `tests/test_livres.py`)

```python
import unittest
from app import create_app
from app.models import db, Livre

class LivreTestCase(unittest.TestCase):
  
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_ajouter_livre(self):
        response = self.client.post('/livres/', json={
            'titre': 'Les Misérables',
            'auteur': 'Victor Hugo'
        })
        self.assertEqual(response.status_code, 201)

    def test_lister_livres(self):
        response = self.client.get('/livres/')
        self.assertEqual(response.status_code, 200)
```

### Explication des sections du `README.md` :

- **Prérequis** : Cela informe les utilisateurs des outils nécessaires avant de démarrer.
- **Installation** : Les étapes pour configurer et exécuter l'application.
- **Démarrer l'application** : Instructions pour lancer le serveur Flask.
- **Utilisation de l'API** : Indique comment interagir avec l'application via des endpoints.
- **Structure du projet** : Aide à comprendre l'organisation des fichiers et dossiers.
- **Tests** : Comment exécuter les tests unitaires pour valider les fonctionnalités.
- **Contribution et Licence** : Pour encourager les contributions et informer sur la licence du projet.

Cela devrait vous donner une bonne base pour documenter et structurer votre projet !
