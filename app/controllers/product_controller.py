from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from app.services.product_service import ProductService
from app.exceptions.product_exceptions import ProductNotFoundError, ValidationError, DatabaseError
from app.validators.input_validators import validate_required_fields, validate_positive_number, validate_possible_fields

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/", methods=["GET"])
def get_products():
    try:
        name = request.args.get('name')
        category = request.args.get('category')
        barcode = request.args.get('barcode')
        price = request.args.get('price')

        if price:
            price = validate_positive_number(price, 'price')
            
        products = ProductService.get_products(name, category, barcode, price)
    
        return jsonify(products), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/<id>", methods=["GET"])
def get_product_by_id(id: int):
    try:
        id = validate_positive_number(id, 'id', require_integer=True)
        product = ProductService.get_product_by_id(id)
        return jsonify(product), 200
    
    except ProductNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@product_bp.route("/", methods=["POST"])
def insert_product():
    
    required_fields = ['name', 'category', 'barcode', 'price']

    try:

        if not request.is_json:
            raise ValidationError("Content-Type must be application/json.")
        
        try:
            data = request.get_json()
        except BadRequest:
            raise ValidationError("Invalid or malformed JSON in request body.")

        
        if not data:
            raise ValidationError("Invalid or missing JSON in request body.")
        
        # Required fields validation
        validate_required_fields(data, required_fields)
        # Price validation
        price = validate_positive_number(data.get('price'), 'price')
        
        product = ProductService.insert_product(
            data.get('name'),
            data.get('category'),
            data.get('barcode'),
            price
        )
        
        return jsonify(product), 201
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/<id>", methods=["DELETE"])
def delete_product(id: int):
    try:
        id = validate_positive_number(id, 'id', require_integer=True)
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
    

@product_bp.route("/<id>", methods=["PUT"])
def update_product(id: int):

    required_fields = ['name', 'category', 'barcode', 'price']

    try:
        id = validate_positive_number(id, 'id', require_integer=True)

        if not request.is_json:
            raise ValidationError("Content-Type must be application/json.")
        
        try:
            data = request.get_json()
        except BadRequest:
            raise ValidationError("Invalid or malformed JSON in request body.")


        if not data:
            raise ValidationError("Invalid or missing JSON in request body.")
        
        # Required fields validation
        validate_required_fields(data, required_fields)
        # Price validation
        price = validate_positive_number(data.get('price'), 'price')
        
        product = ProductService.update_product(
            id,
            data.get('name'),
            data.get('category'),
            data.get('barcode'),
            price
        )

        return jsonify(product), 200
    
    except ProductNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@product_bp.route("/<id>", methods=["PATCH"])
def patch_product(id: int):

    possible_fields = ['name', 'category', 'barcode', 'price']
    required_fields = ['name', 'category', 'barcode', 'price']

    try:
        id = validate_positive_number(id, 'id', require_integer=True)

        if not request.is_json:
            raise ValidationError("Content-Type must be application/json.")
        
        try:
            data = request.get_json()
        except BadRequest:
            raise ValidationError("Invalid or malformed JSON in request body.")


        if not data:
            raise ValidationError("Invalid or missing JSON in request body.")
        
        # Possible fields validation
        validate_possible_fields(data, possible_fields)

        # Price validation
        if "price" in data:
            data["price"] = validate_positive_number(data["price"], 'price')
        
        # Required fields validation
        validate_required_fields(data, required_fields, partial=True)

        product = ProductService.patch_product(id, data)

        return jsonify(product), 200
    
    except ProductNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500