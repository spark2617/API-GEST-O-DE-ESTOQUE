from database import db
from models.supplier import Supplier

class SupplierService:
    
    @staticmethod
    def get_all_suppliers():
        return Supplier.query.all()
    
    @staticmethod
    def get_supplier_by_id(supplier_id):
        return Supplier.query.get(supplier_id)
    
    @staticmethod
    def create_supplier(name, contact_id):
        new_supplier = Supplier(name=name, contact_id=contact_id)
        db.session.add(new_supplier)
        db.session.commit()
        return new_supplier
    
    # precisa alterar essa função
    @staticmethod
    def update_supplier(supplier_id, name=None, contact_id=None):
        supplier = Supplier.query.get(supplier_id)
        if supplier:
            if name:
                supplier.name = name
            if contact_id:
                supplier.contact_id = contact_id
            db.session.commit()
        return supplier
    
    @staticmethod
    def delete_supplier(supplier_id):
        supplier = Supplier.query.get(supplier_id)
        if supplier:
            db.session.delete(supplier)
            db.session.commit()
        return supplier
