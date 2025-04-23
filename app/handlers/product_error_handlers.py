from flask import jsonify
from app.exceptions.product_exceptions import ValidationError, ProductNotFoundError, DatabaseError

def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({"error": str(error)}), 400
    
    @app.errorhandler(ProductNotFoundError)
    def handle_product_not_found_error(error):
        return jsonify({"error": str(error)}), 404
    
    @app.errorhandler(DatabaseError)
    def handle_database_error(error):
        return jsonify({"error": str(error)}), 500
    
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        return jsonify({"error": "An unexpected error occurred:" + str(error)}), 500