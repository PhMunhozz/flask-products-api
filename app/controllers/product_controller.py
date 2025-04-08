from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/", methods=["GET"])
def get_products():
    products = ProductService.get_products()
    
    return jsonify(products), 200

@product_bp.route("/<int:id>", methods=["GET"])
def get_product_by_id(id: int):
    product = ProductService.get_product_by_id(id)

    if product is None:
        return jsonify({"error": f"No product found for id {id}."}), 404
    
    return jsonify(product), 200

@product_bp.route("/<name>", methods=["GET"])
def get_product_by_name(name: str):
    product = ProductService.get_product_by_name(name)

    if product is None:
        return jsonify({"error": f"No product found for name '{name}'."}), 404
    
    return jsonify(product), 200

@product_bp.route("/", methods=["POST"])
def insert_product():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    if not name or not price:
        return {"error": "Product must have 'name' and 'price',"}, 400

    product = ProductService.insert_product(name, price)
    return jsonify(product), 201