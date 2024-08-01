from database import db

from sqlalchemy.orm import relationship
from models.product import product_category

class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    products = relationship('Product', secondary=product_category, back_populates='categories')

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
        
    }

