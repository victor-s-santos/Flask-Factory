def init_app(app):
    """Inicializa as extensões"""

    @app.route("/")
    def index():
        return "Welcome to Home page!"
