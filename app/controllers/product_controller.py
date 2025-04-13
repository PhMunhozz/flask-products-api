from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.exceptions.product_exceptions import ProductNotFoundError, ValidationError, DatabaseError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError


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
    data = request.get_json()
    name = data.get("name")
    category = data.get("category")
    barcode = data.get("barcode")
    price = data.get("price")

    if not name or not category or not barcode or not price:
        raise BadRequest("Product must have 'name', 'category', 'barcode' and 'price'.")
    
    try:
        price = float(price)
    except ValueError:
        raise BadRequest("'Price' must be a valid number.")

    product = ProductService.insert_product(name, price, category, barcode)
    return jsonify(product), 201