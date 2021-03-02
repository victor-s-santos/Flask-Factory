from flask import Flask

def init_app(app: Flask):
    """Inicializa as extensões"""

    @app.route("/")
    def index():
        return "Welcome to Home page!"
