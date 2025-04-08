from app.controllers.product_controller import product_bp

def init_routes(app):
    """Registrando as rotas da aplicação"""
    app.register_blueprint(product_bp)