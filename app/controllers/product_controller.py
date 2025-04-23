from flask import Blueprint, request, jsonify
from app.middlewares.json_validator import validate_json_request
from app.services.product_service import ProductService
from app.validators.input_validators import validate_required_fields, validate_positive_number, validate_possible_fields

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/", methods=["GET"])
def get_products():

    name = request.args.get('name')
    category = request.args.get('category')
    barcode = request.args.get('barcode')
    price = request.args.get('price')

    if price:
        price = validate_positive_number(price, 'price')
        
    products = ProductService.get_products(name, category, barcode, price)

    return jsonify(products), 200
    

@product_bp.route("/<id>", methods=["GET"])
def get_product_by_id(id: int):

    id = validate_positive_number(id, 'id', require_integer=True)
    product = ProductService.get_product_by_id(id)
    return jsonify(product), 200
    

@product_bp.route("/", methods=["POST"])
@validate_json_request
def insert_product(*, data: dict):
    
    required_fields = ['name', 'category', 'barcode', 'price']

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


@product_bp.route("/<id>", methods=["DELETE"])
def delete_product(id: int):

    id = validate_positive_number(id, 'id', require_integer=True)
    ProductService.delete_product(id)

    return jsonify({"message": "Product deleted successfully."}), 200
    

@product_bp.route("/<id>", methods=["PUT"])
@validate_json_request
def update_product(id: int, *, data: dict):

    required_fields = ['name', 'category', 'barcode', 'price']

    id = validate_positive_number(id, 'id', require_integer=True)
    
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
    

@product_bp.route("/<id>", methods=["PATCH"])
@validate_json_request
def patch_product(id: int, *, data: dict):

    possible_fields = ['name', 'category', 'barcode', 'price']
    required_fields = ['name', 'category', 'barcode', 'price']

    id = validate_positive_number(id, 'id', require_integer=True)
    
    # Possible fields validation
    validate_possible_fields(data, possible_fields)

    # Price validation
    if "price" in data:
        data["price"] = validate_positive_number(data["price"], 'price')
    
    # Required fields validation
    validate_required_fields(data, required_fields, partial=True)

    product = ProductService.patch_product(id, data)

    return jsonify(product), 200