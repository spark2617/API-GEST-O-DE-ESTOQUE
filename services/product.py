from database import db
from models.product import Product

class ProductService:
    
    @staticmethod
    def get_all_products():
        products = Product.query.all()
        return [product.to_dict() for product in products]
        
    
    @staticmethod
    def get_product_by_id(product_id):
        product = Product.query.get(product_id) 
        return product.to_dict()
    
    @staticmethod
    def create_product(name, description, price, category_id):
        new_product = Product(name=name, description=description, unitprice=price, category_id=category_id)
        db.session.add(new_product)
        db.session.commit()
        return new_product
    
    @staticmethod
    def update_product(product_id, name=None, description=None, price=None, category_id=None):
        product = Product.query.get(product_id)
        if product:
            if name:
                product.name = name
            if description:
                product.description = description
            if price:
                product.unitprice = price
            if category_id:
                product.category_id = category_id
            db.session.commit()
        return product
    
    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product


