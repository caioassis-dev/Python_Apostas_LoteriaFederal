from flask import Flask
from src.main.routes.siteApostas_routes import apostas_routes_bp

app = Flask(__name__)

app.register_blueprint(apostas_routes_bp)