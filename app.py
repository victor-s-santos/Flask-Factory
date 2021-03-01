import routes
from flask import Flask

def create_app():
    """o programa começa ao chamar esta funcao"""
    app = Flask(__name__)
    routes.init_app(app)
    return app

