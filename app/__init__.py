from flask import Flask
from app.routes import init_routes
from app.handlers.product_error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)

    register_error_handlers(app)
    init_routes(app)

    return app