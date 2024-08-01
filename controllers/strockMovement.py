from flask import Blueprint, request, jsonify
from services.strockMovement import StrockMovementService

strockMovement_bp = Blueprint('strockMovement_bp', __name__)

@strockMovement_bp.route('/stock_movements', methods=['GET'])
def get_stock_movements():
    stock_movements = StrockMovementService.get_all_stock_movements()
    return jsonify([movement.to_dict() for movement in stock_movements])

@strockMovement_bp.route('/stock_movements/<int:movement_id>', methods=['GET'])
def get_stock_movement(movement_id):
    stock_movement = StrockMovementService.get_stock_movement_by_id(movement_id)
    return jsonify(stock_movement.to_dict()) if stock_movement else ('', 404)

@strockMovement_bp.route('/stock_movements/<int:movement_id>', methods=['PUT'])
def update_stock_movement(movement_id):
    data = request.get_json()
    stock_movement = StrockMovementService.update_stock_movement(movement_id, data.get('batch_id'), data.get('movement_type'), data.get('quantity'), data.get('movement_date'))
    return jsonify(stock_movement.to_dict()) if stock_movement else ('', 404)

@strockMovement_bp.route('/stock_movements/<int:movement_id>', methods=['DELETE'])
def delete_stock_movement(movement_id):
    stock_movement = StrockMovementService.delete_stock_movement(movement_id)
    return ('', 204) if stock_movement else ('', 404)