from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/", methods=["GET"])
def get_products():
    name = request.args.get('name')
    price = request.args.get('price')

    products = ProductService.get_products(name, price)
    
    return jsonify(products), 200

@product_bp.route("/<int:id>", methods=["GET"])
def get_product_by_id(id: int):
    product = ProductService.get_product_by_id(id)

    if product is None:
        return jsonify({"error": f"No product found for id {id}."}), 404
    
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