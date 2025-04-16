from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.exceptions.product_exceptions import ProductNotFoundError, ValidationError, DatabaseError
from app.validators.input_validators import validate_required_fields, validate_positive_number

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/", methods=["GET"])
def get_products():
    try:
        name = request.args.get('name')
        category = request.args.get('category')
        barcode = request.args.get('barcode')
        price = request.args.get('price')

        products = ProductService.get_products(name, category, barcode, price)
    
        return jsonify(products), 200
    
    except Exception as e:
        return jsonify(error=str(e)), 500


@product_bp.route("/<id>", methods=["GET"])
def get_product_by_id(id: int):
    try:
        product = ProductService.get_product_by_id(id)
        return jsonify(product), 200
    
    except ProductNotFoundError as e:
        return jsonify(error=str(e)), 404
    
    except ValidationError as e:
        return jsonify(error=str(e)), 400
    
    except DatabaseError as e:
        return jsonify(error=str(e)), 500
    
    except Exception as e:
        return jsonify(error=str(e)), 500
    

@product_bp.route("/", methods=["POST"])
def insert_product():
    
    required_fields = ['name', 'category', 'barcode', 'price']

    try:
        data = request.get_json()
        
        if not data:
            raise ValidationError("Invalid or missing JSON in request body.")
        
        # Required fields validation
        validate_required_fields(data, required_fields)
        # Price validation
        validate_positive_number(data.get('price'), 'price')
        
        product = ProductService.insert_product(
            data.get('name'),
            data.get('category'),
            data.get('barcode'),
            data.get('price')
        )
        
        return jsonify(product), 201
    
    except ValidationError as e:
        return jsonify(error=str(e)), 400
    
    except DatabaseError as e:
        return jsonify(error=str(e)), 400
    
    except Exception as e:
        return jsonify(error=str(e)), 500


@product_bp.route("/<id>", methods=["DELETE"])
def delete_product(id: int):
    try:
        validate_positive_number(id, 'id', require_integer=True)
        ProductService.delete_product(id)

        return jsonify({"message": "Product deleted successfully."}), 200
    
    except ProductNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500