from flask import Flask
from flask_cors import CORS
from .routes.scholarships import scholarships_bp
from .routes.health import health_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(JSON_SORT_KEYS=False)
    if config:
        app.config.update(config)
    CORS(app)
    app.register_blueprint(health_bp)
    app.register_blueprint(scholarships_bp, url_prefix="/api/v1/scholarships")
    return app
