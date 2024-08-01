from flask import Blueprint, request, jsonify
from services.supplier import SupplierService

supplier_bp = Blueprint('supplier_bp', __name__)

@supplier_bp.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers = SupplierService.get_all_suppliers()
    return jsonify([supplier.to_dict() for supplier in suppliers])

@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    supplier = SupplierService.get_supplier_by_id(supplier_id)
    return jsonify(supplier.to_dict()) if supplier else ('', 404)

@supplier_bp.route('/suppliers', methods=['POST'])
def create_supplier():
    data = request.get_json()
    supplier = SupplierService.create_supplier(data['name'], data['contact_id'])
    return jsonify(supplier.to_dict()), 201

@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    data = request.get_json()
    supplier = SupplierService.update_supplier(supplier_id, data.get('name'), data.get('contact_id'))
    return jsonify(supplier.to_dict()) if supplier else ('', 404)

@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id):
    supplier = SupplierService.delete_supplier(supplier_id)
    return ('', 204) if supplier else ('', 404)