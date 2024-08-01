from flask import Blueprint, request, jsonify
from services.product import ProductService

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        products = ProductService.get_all_products()
        return jsonify(products)
    except Exception as error:
        return error


@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product_by_id(product_id)
    return jsonify(product) if product else ('', 404)

@product_bp.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    product = ProductService.create_product(data['name'], data.get('description'), data['unitprice'], data['category_id'])
    return jsonify(product.to_dict()), 201

@product_bp.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = ProductService.update_product(product_id, data.get('name'), data.get('description'), data.get('unitprice'), data.get('category_id'))
    return jsonify(product.to_dict()) if product else ('', 404)

@product_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = ProductService.delete_product(product_id)
    return ('', 204) if product else ('', 404)
