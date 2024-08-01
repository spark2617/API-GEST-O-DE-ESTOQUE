from flask import Blueprint, request, jsonify
from services.batch import BatchService

batch_bp = Blueprint('batch_bp', __name__)

@batch_bp.route('/batches', methods=['GET'])
def get_batches():
    batches = BatchService.get_all_batches()
    return jsonify([batch.to_dict() for batch in batches])

@batch_bp.route('/batches/<int:batch_id>', methods=['GET'])
def get_batch(batch_id):
    batch = BatchService.get_batch_by_id(batch_id)
    return jsonify(batch.to_dict()) if batch else ('', 404)

@batch_bp.route('/batches', methods=['POST'])
def create_batch():
    data = request.get_json()
    batch = BatchService.create_batch(data['product_id'], data['batch_code'], data['arrival_date'], data['expiration_date'], data['quantity'])
    return jsonify(batch.to_dict()), 201

@batch_bp.route('/batches/<int:batch_id>', methods=['PUT'])
def update_batch(batch_id):
    data = request.get_json()
    batch = BatchService.update_batch(batch_id, data.get('product_id'), data.get('batch_code'), data.get('arrival_date'), data.get('expiration_date'), data.get('quantity'))
    return jsonify(batch.to_dict()) if batch else ('', 404)

@batch_bp.route('/batches/<int:batch_id>', methods=['PUT'])
def update_batch(batch_id):
    data = request.get_json()
    batch = BatchService.batchEntryOrExit(batch_id, data.get('quantity'))
    return jsonify(batch.to_dict()) if batch else ('', 404)

@batch_bp.route('/batches/<int:batch_id>', methods=['DELETE'])
def delete_batch(batch_id):
    batch = BatchService.delete_batch(batch_id)
    return ('', 204) if batch else ('', 404)