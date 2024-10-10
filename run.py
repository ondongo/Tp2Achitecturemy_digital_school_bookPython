from flask import Flask, request
from flask_restx import Api
from app import create_app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True)
