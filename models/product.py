from database import db

# tabela de associação muitos para muitos
from sqlalchemy import Table, Column, Integer, ForeignKey

product_category = Table('product_category', db.Model.metadata,
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('category.id'), primary_key=True)
)


from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    unitprice = db.Column(db.Float, nullable=False) 
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    
    supplier = relationship('Supplier')
    categories = relationship('Category', secondary='product_category')
    batches = relationship('Batch')

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'price': self.unitprice,
        'supplier_id': self.supplier_id,
        'categories': [category.name for category in self.categories],
        'batches': [{
            'id': batch.id,
            'code': batch.batch_code,
            'arrival_date': batch.arrival_date,
            'expiration_date': batch.expiration_date,
            'quantity': batch.quantity
        } for batch in self.batches]
    }
     