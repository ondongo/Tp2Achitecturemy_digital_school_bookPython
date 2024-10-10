import os

class Config:
    APP_NAME = "BiblioMydigitalSchool"
    
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'biblio.sqlite')}"
    
    SECRET_KEY = "SecretKey"
