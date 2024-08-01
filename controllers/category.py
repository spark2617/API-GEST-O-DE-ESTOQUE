from services.category import CategoryService
from flask import Blueprint, request, jsonify

category_bp = Blueprint('product_bp', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = CategoryService.get_all_categories()
    return jsonify([category.to_dict() for category in categories])

@category_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = CategoryService.get_category_by_id(category_id)
    return jsonify(category.to_dict()) if category else ('', 404)

@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category = CategoryService.create_category(data['name'])
    return jsonify(category.to_dict()), 201

@category_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    category = CategoryService.update_category(category_id, data.get('name'))
    return jsonify(category.to_dict()) if category else ('', 404)

@category_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = CategoryService.delete_category(category_id)
    return ('', 204) if category else ('', 404)
